FROM python:3.10-slim

WORKDIR /opt
COPY src setup.py requirements.txt pyproject.toml /opt/

RUN pip install .

CMD [ "chatta" ]
