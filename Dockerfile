FROM python:3.10-slim

# Install git
RUN apt-get update && apt-get install -y git && apt-get clean

WORKDIR /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Cloud Run expects your app to listen on PORT (default 8080)
ENV PORT=8080
EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
