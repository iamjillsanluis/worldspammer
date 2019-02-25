import os
from celery import Celery
from celery.schedules import crontab


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
    task_serializer="json",
    accept_content=["json"],  # Ignore other content
    result_serializer="json",
)


app.conf.beat_schedule = {
    "spam-the-world": {
        "task": "worldspammer.workers.tasks.spammer.spam_bomb",
        "schedule": crontab(hour="*/1", minute=0),
    },
}


if __name__ == "__main__":
    app.start()
