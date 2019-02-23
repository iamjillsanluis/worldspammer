from datetime import datetime

with open("scheduler.tmp", "w+") as fh:
    fh.write(datetime.now().isoformat())
