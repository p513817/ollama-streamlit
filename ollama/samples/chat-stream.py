BASE_URL = "http://127.0.0.1:8000"
import json

import httpx

host = "localhost"
port = 11434
url = f"http://{host}:{str(port)}/api/chat"
model_name = "llama3.1:8b"
data = {
    "model": model_name,
    "messages": [{"role": "user", "content": "what is python?"}],
}
print(url, data, type(data))

with httpx.stream("POST", url=url, json=data) as response:
    if response.headers.get("Transfer-Encoding") == "chunked":
        print("Response is a streaming response")

        for chunk in response.iter_lines():
            # print(chunk)
            print(json.loads(chunk)["message"]["content"], end=" ", flush=True)

    else:
        print("Response is not a streaming response")
