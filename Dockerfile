FROM python:3.10-slim

# Install git
RUN apt-get update && apt-get install -y git && apt-get clean

WORKDIR /app
COPY . /app

# Define build argument for the token
ARG GITHUB_TOKEN
ENV GITHUB_TOKEN=${GITHUB_TOKEN}

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

ENV PORT=8080
EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
