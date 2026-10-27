import sys
import os
import json
from datetime import datetime

TASKS_FILE = "tasks.json"



def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []

    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):

    with open(TASKS_FILE,"w", encoding="utf-8") as f:
        json.dump(tasks,f,indent=4)


def add_task(description):
    tasks = load_tasks()

    if tasks:
        ids = []
        for task in tasks:
            ids.append(task["id"])
        biggest = max(ids) 
        new_id = biggest + 1
    else:
        new_id = 1

    now = datetime.now().isoformat()
    new_task = {
        "id": new_id,
        "description": description,
        "createdAt": now,
        "updatedAt": now,
    }
    tasks.append(new_task)
    save_tasks(tasks= tasks)
    print(f"Task added succesfully (ID: {new_id}) ")

def main():
    # Kullanıcı hiç komut yazmadıysa
    if len(sys.argv) < 2:
        print(f'Usage: python task_cli.py add "Buy groceries"')
        return

    command = sys.argv[1]

    if command == "add":
       if len(sys.argv) < 3:
            print(f"Error: please input a description")
            print(f'xample: python task_cli.py <command> "[arguments]"')
       else:
            add_task(sys.argv[2])
    elif command == "list":
        print("list komutu calisti")
    else:
        print(f"Bilinmeyen komut: {command}")

    


if __name__ == "__main__":
    main()