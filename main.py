import os
import threading
import pika
import functools

from messaging.gitlab_rabbitmq_consumer import GitLabConsumer
import coloredlogs
from dotenv import load_dotenv
import logging

load_dotenv()
coloredlogs.install()

log = logging.getLogger("main.py")

log.info(f"Starting GitLab service")
load_dotenv()

gitlab_consumer = GitLabConsumer()


def on_message(channel, method_frame, header_frame, body, args):
    (connection, threads) = args
    delivery_tag = method_frame.delivery_tag
    t = threading.Thread(target=gitlab_consumer.consume_gitlab_data, args=(connection, channel, delivery_tag, body))
    t.start()
    threads.append(t)


# port=os.getenv('RABBIT_PORT') --> for local development
credentials = pika.PlainCredentials(os.getenv('RABBIT_USR'), os.getenv('RABBIT_PWD'))
parameters = pika.ConnectionParameters(host=os.getenv('RABBIT_HOST'),
                                       credentials=credentials, heartbeat=5)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange="plugins", exchange_type="direct", passive=False, durable=True, auto_delete=False)
channel.queue_declare(queue="gitlab", auto_delete=False)
channel.queue_bind(exchange="plugins", queue="gitlab", routing_key="gitlab")
channel.basic_qos(prefetch_count=1)

threads = []
on_message_callback = functools.partial(on_message, args=(connection, threads))
channel.basic_consume(queue="gitlab", on_message_callback=on_message_callback)

try:
    log.info(f"GitLab service started")
    channel.start_consuming()
except KeyboardInterrupt:
    log.info(f"GitLab service stopped")
    channel.stop_consuming()

# Wait for all to complete
for thread in threads:
    thread.join()
