import pika
from django.http import HttpResponse


def send_message_view(request):
    message = "HELLO WORLD!"
    send_message(message)
    return HttpResponse(f"Сообщение отправлено: {message}")


def send_message(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='my_queue')
    channel.basic_publish(exchange='', routing_key='my_queue', body=message)
    connection.close()
