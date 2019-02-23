from datetime import datetime

with open("app.tmp", "w+") as fh:
    fh.write(datetime.now().isoformat())
