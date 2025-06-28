FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "-u", "agent.py"]
git+https://github.com/google/agent-development-kit.git
