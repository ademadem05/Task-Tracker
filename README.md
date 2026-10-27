# Task Tracker CLI

A simple command-line application to track and manage your tasks. You can add, update, and delete tasks, mark them as in progress or done, and list them by status. All tasks are saved in a local JSON file.

This project is based on the [roadmap.sh Task Tracker project](https://roadmap.sh/projects/task-tracker).

## Features

- Add, update, and delete tasks
- Mark tasks as `in-progress` or `done`
- List all tasks or filter them by status
- Tasks are saved automatically to a JSON file
- Handles invalid input without crashing

## Requirements

- Python 3.x
- No external libraries, only Python's standard library

## Installation

```bash
git clone https://github.com/ademadem05/Task-Tracker.git
cd Task-Tracker
```

## Usage

```bash
# Add a new task
python task_cli.py add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Update a task's description
python task_cli.py update 1 "Buy groceries and cook dinner"

# Delete a task
python task_cli.py delete 1

# Mark a task as in progress or done
python task_cli.py mark-in-progress 1
python task_cli.py mark-done 1

# List all tasks
python task_cli.py list

# List tasks by status
python task_cli.py list todo
python task_cli.py list in-progress
python task_cli.py list done
```

Example output of `list`:

```
[1] Buy groceries (done)
[2] Study math (in-progress)
[3] Wash the dishes (todo)
```

## Task Properties

Each task is stored with the following properties:

| Property      | Description                                      |
|---------------|--------------------------------------------------|
| `id`          | A unique number that identifies the task         |
| `description` | A short description of the task                  |
| `status`      | The task's status: `todo`, `in-progress`, `done` |
| `createdAt`   | The date and time the task was created           |
| `updatedAt`   | The date and time the task was last updated      |

Example:

```json
{
    "id": 1,
    "description": "Buy groceries",
    "status": "todo",
    "createdAt": "2026-10-27T14:05:31.123456",
    "updatedAt": "2026-10-27T14:05:31.123456"
}
```

## Data Storage

Tasks are stored in a `tasks.json` file in the current directory. If the file does not exist, it is created automatically when you add your first task.

## Error Handling

The application shows a clear error message instead of crashing when:

- A command is missing required arguments
- A task ID is not a number
- A task with the given ID does not exist
- An invalid status is used with `list`
- An unknown command is entered