import json
import re

import httpx
from chatta_app.schema.message import OllamaMessage, OllamaRequestData


def is_valid_ip(ip: str) -> bool:
    """Regex pattern for matching a valid IP address"""
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return pattern.match(ip) is not None


def get_chat_route(host: str, port: int) -> str:
    if not is_valid_ip(host):
        raise TypeError("Httpx only support regular IP address, like AAA.BBB.CCC.DDD")
    return f"http://{host}:{port}/api/chat"


def get_request_data(model: str, messages: list[str], role: str) -> OllamaRequestData:
    return OllamaRequestData(
        model=model,
        messages=[OllamaMessage(role=role, content=message) for message in messages],
    )


def stream_chat(url: str, data: OllamaRequestData):
    with httpx.stream("POST", url=url, json=data.model_dump()) as response:
        if response.headers.get("Transfer-Encoding") == "chunked":
            for chunk in response.iter_lines():
                yield json.loads(chunk)["message"]["content"]
        else:
            raise RuntimeError(json.loads(response.read().decode("utf-8")))
