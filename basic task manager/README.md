# todo CLI

### Introduction
Program a simple CLI-based todo application 

The application has the commands

### `init` command
Usage `init`

Use this command to setup and do any necessary initialization such as creating a file.

After running the command, print out `Initialized successfully.`

If any other command is ran before running the `init` command, prompt the user with the message `Please run 'todo init' before running '<command-name>' command.`

### `list` command
Usage `list`

Output all tasks in the current todo list, the list is divided into two ie `To be done` and `Completed`. Each task starts with the task ID

### `add` command
Usage `add <task name>`

This command adds new tasks to the task list

### `mark` command
Usage `mark <task ID>`

Marks the task Completed

