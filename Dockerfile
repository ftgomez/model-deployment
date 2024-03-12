FROM --platform=linux/x86_64 python:3.11

WORKDIR /app

COPY src/__init__.py /app/src/__init__.py
COPY src/runners.py /app/src/runners.py
COPY src/services.py /app/src/services.py
COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

ARG BENTO_SERVICE_NAME
ENV BENTO_SERVICE_NAME=$BENTO_SERVICE_NAME

CMD BENTOML_PORT=8000 bentoml serve src/services.py:${BENTO_SERVICE_NAME}
