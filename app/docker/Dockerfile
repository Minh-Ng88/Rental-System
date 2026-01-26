FROM python:3.10-slim

WORKDIR /app

COPY . .

ENV PYTHONPATH=/app/app

RUN pip install --no-cache-dir pytest

CMD ["pytest", "test", "-v"]
