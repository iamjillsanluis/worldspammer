import os
from celery import Celery


app = Celery(
    "worldspammer",
    broker="amqp://{}:{}@rabbitmq:5672/{}".format(
        os.environ["RABBITMQ_DEFAULT_USER"],
        os.environ["RABBITMQ_DEFAULT_PASS"],
        os.environ["RABBITMQ_DEFAULT_VHOST"],
    ),
    include=["worldspammer.workers.tasks.spammer"]
)

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == "__main__":
    app.start()
