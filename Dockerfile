FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py /app/main.py
EXPOSE 8080
CMD ["python", "main.py", "-c", "/app/config.json"]
