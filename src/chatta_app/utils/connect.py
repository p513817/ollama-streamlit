import os


def get_ollama_host(keyword: str = "OLLAMA_HOST", default: str = "127.0.0.1") -> str:
    return os.environ.get(keyword, default)


def get_ollama_port(keyword: str = "OLLAMA_PORT", default: str = "11434") -> int:
    return int(os.environ.get(keyword, default))


def get_ollama_model(
    keyword: str = "OLLAMA_MODEL", default: str = "llama3.1:8b"
) -> str:
    return os.environ.get(keyword, default)
