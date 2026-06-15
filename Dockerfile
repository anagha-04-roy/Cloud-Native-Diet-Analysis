# ---- Stage 1: Build environment ----
FROM python:3.9-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---- Stage 2: Final lightweight image ----
FROM python:3.9-slim

WORKDIR /app

COPY data_analysis.py .
COPY --from=builder /usr/local/lib/python3.9 /usr/local/lib/python3.9

CMD ["python", "data_analysis.py"]
