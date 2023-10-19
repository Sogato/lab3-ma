import pika
import logging

logging.basicConfig(level=logging.INFO)


def callback(ch, method, properties, body):
    logging.info(f"Полученноe сообщение: {body}")


parameters = pika.ConnectionParameters(host='rabbitmq')
connection = pika.BlockingConnection(parameters=parameters)
channel = connection.channel()
channel.queue_declare(queue='my_queue')
channel.basic_consume(queue='my_queue', on_message_callback=callback, auto_ack=True)

logging.info('Ожидание сообщений. Для выхода нажмите CTRL+C')
channel.start_consuming()
