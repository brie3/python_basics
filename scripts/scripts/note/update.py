import os
import json
from datetime import datetime, date, time, timezone


def update(path):
    id = int(input('input record id to update\n'))
    f = open(path, 'r+', encoding='utf-8')
    found = False
    if os.stat(path).st_size > 0:
        data = json.load(f)
        i = 0
        for line in data:
            if id == line["id"]:
                data[i]["header"] = input('input header\n')
                data[i]["body"] = input('input body\n')
                data[i]["updated_at"] = datetime.now()
                found = True
                break
            i += 1
    if not found:
        print("record not found")
        return
    f.seek(0)
    json.dump(data, f,  indent=2, default=str)
    f.truncate()
