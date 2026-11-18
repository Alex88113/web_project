FROM python:3.13-slim
WORKDIR /src

RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
COPY ./src .

RUN adduser --disabled-password --gecos '' appuser && chown -R appuser .
USER appuser

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]