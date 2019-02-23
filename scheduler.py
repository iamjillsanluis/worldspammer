import pendulum
from worldspammer.core import applicable_timezones
from worldspammer.workers.tasks.spammer import notify_timezone


for timezone in applicable_timezones():
    local_time = pendulum.now(timezone)
    notify_timezone.delay(timezone, local_time.to_date_string())
