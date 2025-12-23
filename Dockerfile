FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Install awscli (optional)
RUN apt-get update && apt-get install -y awscli && rm -rf /var/lib/apt/lists/*

CMD ["python", "app.py"]
