FROM python:3.12-slim
WORKDIR /app

# install deps first (better build cache)
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# app code
COPY app/ .

# run FastAPI with uvicorn on 8000 (container-internal)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
