FROM --platform=linux/arm64/v8 python:3.11

WORKDIR /app

COPY src/__init__.py /app/src/__init__.py
COPY src/runners.py /app/src/runners.py
COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

CMD [ "bentoml", "serve", "src.runners" ]