import os
import json
import operator


def read(path):
    f = open(path, 'r', encoding='utf-8')
    if os.stat(path).st_size > 0:
        data = json.load(f)
        data.sort(key=operator.itemgetter('created_at'))
        print(json.dumps(data, indent=2))
    else:
        print('[]')
