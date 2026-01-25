FROM python:3.12-slim

WORKDIR /app

# Copy requirements từ thư mục app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ source code
COPY app .

# Cài pytest
RUN pip install --no-cache-dir pytest

# Chạy test tự động
CMD ["pytest", "test", "-v"]
