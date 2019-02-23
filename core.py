import pendulum
import pytzdata


def applicable_timezones(local_hour_notification=3, timezones=pytzdata.timezones):
    for timezone in timezones:
        local_notification_time = pendulum.now(timezone)
        if local_notification_time.hour == local_hour_notification:
            yield timezone
