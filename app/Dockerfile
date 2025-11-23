FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy requirements first -> better caching
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . /app/

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
