import functools
import json
import threading

from services.gitlab_service import GitLabService
import logging

log = logging.getLogger("messaging/gitlab_rabbitmq_consumer.py")


class RabbitMQConsumer:
    def __init__(self):
        self.gitlab_service = GitLabService()

    def ack_message(self, channel, delivery_tag):
        """Note that `channel` must be the same pika channel instance via which
        the message being ACKed was retrieved (AMQP protocol constraint).
        """
        if channel.is_open:
            channel.basic_ack(delivery_tag)
        else:
            # Channel is already closed, so we can't ACK this message;
            pass

    def consume_gitlab_data(self, connection, channel, delivery_tag, body):
        """Consumes the data to of all the GitLab commands"""
        body = json.loads(body)
        event_type = body['event_type']
        log.info(f"Consumed the data from the GitLab queue: Thread ID: {threading.get_ident()}, "
                 f"Delivery tag: {delivery_tag}, Body: {body}")

        if event_type == "create_mr":
            self.gitlab_service.create_mr(body)
        elif event_type == "create_r":
            self.gitlab_service.create_r(body)
        elif event_type == "create_i":
            self.gitlab_service.create_i(body)
        elif event_type == "close_i":
            self.gitlab_service.close_i(body)

        cb = functools.partial(self.ack_message, channel, delivery_tag)
        connection.add_callback_threadsafe(cb)
