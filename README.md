# Chatta: ollama-with-streamlit
A chatbot demo with Streamlit and Ollama

# Pre-requirement
* Docker Engine
* GPU Driver
* NVIDIA Container Toolkit

# Quick Start
```bash
docker compose -f simple-chatta.yaml up
```

# Install from source
* Prepare environments
    ```bash
    python3 -m venv .env
    source .env/bin/activate
    ```
* Installation
    ```bash
    pip install .
    # if you want ot modify the source code then use `pip install -e .`
    ```

# Distribution
```bash
python3 -m pip install --upgrade build
python3 -m build
```

Introduce 3ME3 in 100 words; if you don't know, just tell me, 'I dont known'.