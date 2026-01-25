FROM python:3.12-slim

WORKDIR /app

# Copy requirements từ thư mục app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app .

RUN pip install --no-cache-dir pytest

CMD ["pytest", "test", "-v"]
