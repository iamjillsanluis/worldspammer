from datetime import datetime

with open("worker.tmp", "w+") as fh:
    fh.write(datetime.now().isoformat())
