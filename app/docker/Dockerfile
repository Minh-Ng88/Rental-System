FROM python:3.12-slim

WORKDIR /app

# Copy requirements nếu có (nếu chưa, tạo file requirements.txt riêng)
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ code từ repo
COPY . .

# Cài pytest nếu test dùng pytest (hoặc unittest thì không cần)
RUN pip install --no-cache-dir pytest

# Chạy test tự động (giả sử test nằm trong thư mục test/)
CMD ["pytest", "test/", "-v"]
