import logging
import pendulum
import pytzdata
from pendulum.tz.zoneinfo.exceptions import InvalidPosixSpec


log = logging.getLogger(__name__)


def applicable_timezones(local_hour_notification=3, timezones=pytzdata.timezones):
    for timezone in timezones:
        try:
            local_notification_time = pendulum.now(timezone)
            if local_notification_time.hour == local_hour_notification:
                yield timezone
        except InvalidPosixSpec:
            log.warn("Cannot analyze timezone %s", timezone)
