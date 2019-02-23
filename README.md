# World Spammer
A very simple proof of concept demonstrating how to execute daily tasks based on your target's local day.

A sample use case is, sending your subscribers around the world of yesterday's local hottest news. The program correctly sends our Australian subscribers their daily digest ahead of our North American subscribers.


## Getting Started
1. Make sure you have Docker installed
2. Clone this repository
3. (Optional) Fill in your SLACK information in the `.env` file
4. Run `docker-compose up -d`

## How it works?
1. Every hour, Celery Beat runs the `spam_bomb` task which identifies which timezones to notify
2. For each of the timezone notified, if you have configured the `SLACK` settings correctly in your `.env` file, it should start sending you message in your target channel. Otherwise, the message is sent to log. 

To monitor the log, you can run `docker-compose logs -f`. 

Tip: You can also limit the logs to specific service. For example, to limit the logs to scheduler, you can run `docker-compose logs -f scheduler`.  
 
 
## Tools
To accomplish this, I've used the following robust libraries:
* [Celery](http://docs.celeryproject.org/en/latest/) - a distributed task queue
* [Celery Beat](http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html) - a scheduler for Celery tasks
* [RabbitMQ](https://www.rabbitmq.com/) - broker for Celery Tasks


For development
* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)
