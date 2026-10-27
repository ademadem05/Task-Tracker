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
        "status": "todo",
        "createdAt": now,
        "updatedAt": now,
    }
    tasks.append(new_task)
    save_tasks(tasks= tasks)
    print(f"Task added succesfully (ID: {new_id}) ")

def list_tasks(status=None):
    tasks = load_tasks()

    if tasks:
        if status == None:
            for task in tasks:
                print(f"[{task["id"]}] {task["description"]} ({task['status']})")
        else:
            for task in tasks:
                if task["status"] == status:
                   print(f"[{task['id']}] {task['description']} ({task['status']})") 
    else:
        print(f"Upload the tasks, the list is empty")

def mark_task(task_id, new_status):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as {new_status}")
            return

    print(f"Task with ID {task_id} not found")

def delete(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print(f"Task {task_id} deleted successfully")
            return
    print(f"Task {task_id} is not found")

def update(task_id, new_task):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_task
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully")
            return
    print(f"Task {task_id} is not found")

def main():
    # Kullanıcı hiç komut yazmadıysa
    if len(sys.argv) < 2:
        print(f'Usage: python task_cli.py add "Buy groceries"')
        return

    command = sys.argv[1]

    if command == "add":
       if len(sys.argv) < 3:
            print(f"Error: please input a description")
            print(f'Example: python task_cli.py <command> "[arguments]"')
       else:
            add_task(sys.argv[2])
    elif command == "list":
        if len(sys.argv) < 3:
             list_tasks()       
        else:
            list_tasks(sys.argv[2])
    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Error: please provide a task ID")
            print("Example: python task_cli.py mark-in-progress 1")
        else:
            task_id = int(sys.argv[2])
            mark_task(task_id, "in-progress")

    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Error: please provide a task ID")
            print("Example: python task_cli.py mark-done 1")
        else:
            task_id = int(sys.argv[2])
            mark_task(task_id, "done")

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: please provide a task ID")
            print("Example: python task_cli.py delete 1")
        else:
            task_id = int(sys.argv[2])
            delete(task_id)
    elif command == "update":
        if len(sys.argv) < 4:
            print("Error: please provide a task ID")
            print('Example: update 1 "Buy groceries and cook dinner"')
        else:
             task_id = int(sys.argv[2])
             new_description = sys.argv[3]
             update(task_id, new_description )
    else:
        print("Command not found")
        print("available commands: add, update, delete, list, mark-done, mark-in-progress")
        

    


if __name__ == "__main__":
    main()