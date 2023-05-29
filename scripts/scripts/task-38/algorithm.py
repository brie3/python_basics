import os
from print_records import *
from upsert_record import *
from search_record import *
from delete_record import *

actions = {
    "1": "print",
    "2": "input",
    "3": "search",
    "4": "delete",
    "q": "quit"
}

action = None

path = 'phone_book.txt'
if not os.path.exists(path):
    os.mknod(path)

while True:
    print("What should i do?", *[f"{i} - {actions[i]}" for i in actions])
    action = input()
    if action == "1":
        print_records(path)
    elif action == "2":
        upsert_record(path)
    elif action == "3":
        search_record(path)
    elif action == "4":
        delete_record(path)
    elif action == "q":
        break
    else:
        continue
