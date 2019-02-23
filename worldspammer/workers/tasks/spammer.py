import os
import logging

from worldspammer.workers.celery import app


log = logging.getLogger(__name__)


@app.task
def notify_timezone(timezone, target_date):
    slack_token = os.environ["SLACK_API_TOKEN"]
    slack_channel = os.environ["SLACK_CHANNEL"]

    message = ":smiling_imp: Notify our friends in {} for events for {}! :tada:".format(timezone, target_date)

    if slack_token and slack_channel:
        from slackclient import SlackClient
        client = SlackClient(slack_token)

        client.api_call(
            "chat.postMessage",
            channel=slack_channel,
            text=message
        )
    else:
        log.info(message)
