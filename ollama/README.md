
1. Prepare Llama3.1
    ```bash
    curl --location 'http://localhost:11434/api/pull' \
    --data '{
        "name": "llama3.1:8b",
        "stream": false
    }'
    ```
2. Check Model List ( [api/tags](http://127.0.0.1:11434/api/tags) )
    ```json
    {
    "models": [
        {
        "name": "llama3.1:8b",
        "model": "llama3.1:8b",
        "modified_at": "2024-08-06T02:36:54.542034902Z",
        "size": 4661226402,
        "digest": "62757c860e01d552d4e46b09c6b8d5396ef9015210105427e05a8b27d7727ed2",
        "details": {
            "parent_model": "",
            "format": "gguf",
            "family": "llama",
            "families": [
            "llama"
            ],
            "parameter_size": "8.0B",
            "quantization_level": "Q4_0"
        }
        }
    ]
    }
    ```