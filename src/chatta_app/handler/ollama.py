import json
import time
from collections.abc import Generator

import httpx
from chatta_app.schema.message import OllamaMessage, OllamaRequestData
from chatta_app.utils.chat import get_chat_route
from chatta_app.utils.connect import get_ollama_host, get_ollama_model, get_ollama_port


class OllamaHandler:
    def __init__(self) -> None:
        self.host = get_ollama_host()
        self.port = get_ollama_port()
        self.model = get_ollama_model()
        self.chat_api = get_chat_route(self.host, self.port)
        self.current_messages = []

        self._check_connection()
        self._warmup()

    def _check_connection(self, count_times: int = 10) -> None:
        url = f"http://{self.host}:{self.port}/api/tags"
        error = ""
        while count_times >= 0:
            try:
                response = httpx.get(url)
                response.raise_for_status()
                break
            except Exception as e:
                error = e
            count_times -= 1
            time.sleep(1)
        if count_times <= 0:
            raise RuntimeError(
                f"Ensure the Ollama Server is Launched. \n\t{self.host}:{self.port} ({error})"
            )

    def _warmup(self):
        self.add_message(content="just for warmup", role="user")
        self.stream_chat()

    def add_message(self, content: str, role: str = "user") -> None:
        self.current_messages.append(OllamaMessage(role=role, content=content))

    def stream_chat(self) -> Generator[str] | None:
        if self.current_messages == []:
            print("There is no current messages")
            return
        data = OllamaRequestData(
            model=self.model, messages=self.current_messages
        ).model_dump()
        with httpx.stream("POST", url=self.chat_api, json=data) as response:
            if response.headers.get("Transfer-Encoding") == "chunked":
                for chunk in response.iter_lines():
                    yield json.loads(chunk)["message"]["content"]
            else:
                raise RuntimeError(json.loads(response.read().decode("utf-8")))

        self.current_messages.clear()
