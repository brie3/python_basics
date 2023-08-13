import os
import json
from datetime import datetime, date, time, timezone


def add(path):
    id = 0
    data = []
    f = open(path, 'r+', encoding='utf-8')
    if os.stat(path).st_size > 0:
        data = json.load(f)
        for line in data:
            id = line["id"]
    record = {"id": id+1}
    record["header"] = input('input header\n')
    record["body"] = input('input body\n')
    current = datetime.now()
    record["created_at"] = current
    record["updated_at"] = current
    data.append(record)
    f.seek(0)
    json.dump(data, f,  indent=2, default=str)
    f.truncate()
