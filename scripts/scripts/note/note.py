import os
import json
from read import *
from add import *
from update import *
from delete import *

actions = {
    "1": "read",
    "2": "add",
    "3": "update",
    "4": "delete",
    "q": "quit"
}

action = None

path = 'notes.txt'
if not os.path.exists(path):
    os.mknod(path)

while True:
    print("What should i do?", *[f"{i} - {actions[i]}" for i in actions])
    action = input()
    if action == "1":
        read(path)
    elif action == "2":
        add(path)
    elif action == "3":
        update(path)
    elif action == "4":
        delete(path)
    elif action == "q":
        break
    else:
        continue
