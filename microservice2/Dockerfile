FROM python:3.11.5

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Устанавливаем инструмент ожидания (например, wait-for-it)
RUN apt-get update && apt-get install -y wait-for-it

# Команда по умолчанию для запуска обработчика сообщений с ожиданием RabbitMQ
CMD ["wait-for-it", "--timeout=30", "rabbitmq:5672", "--", "python", "worker.py"]
