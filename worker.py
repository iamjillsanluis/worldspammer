from celery import Celery

app = Celery('worker', broker='amqp://homer:doh@rabbitmq:5672/springfield')


@app.task
def add(x, y):
    return x + y
