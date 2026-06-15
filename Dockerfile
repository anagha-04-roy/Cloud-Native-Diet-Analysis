# ---- Build environment----
FROM python:3.9-slim AS builder
 
WORKDIR /app
 
# Install dependencies separately for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
 
# ------Final lightweight image ----
FROM python:3.9-slim
 
WORKDIR /app
 
# Copy only necessary files
COPY data_analysis.py .
COPY --from=builder /usr/local/lib/python3.9 /usr/local/lib/python3.9
 
# Run the script
CMD ["python", "data_analysis.py"]

