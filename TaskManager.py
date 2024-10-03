import math

from prettytable import PrettyTable

# Task manager
task = {}
table = PrettyTable()
table.field_names = ["Task Number", "Task", "Progression"]


# Add a task
def adding():
    l = task
    t = input("Enter Task's label:\n")
    n = int(input(f"If you have any progress on {t} enter number\t1\n"))
    if n == 1:
        p = int(input("Enter how many percent of the task have you done:\n"))
        while p not in range(0, 101):
            p = int(input("Enter a valid percent in range of 0 to 99:\n"))
        l[t] = p
    else:
        l[t] = 0


# Delete a task
def deleting():
    l = task
    keys = list(l.keys())
    n = int(input("Enter the task number you want to Delete:\n"))
    while n not in range(1, len(keys) + 1):
        n = int(input("Enter a valid task number:\n"))
    l.pop(keys[n - 1])


# Update a task
def update():
    l = task
    n = int(input("Enter the task number you want to Update:\n"))
    keys = list(l.keys())
    while n not in range(1, len(keys) + 1):
        n = int(input("Enter a valid task number:\n"))
    l[keys[n - 1]] = int(input("Enter the percentage of the task:\n"))


# Editing a Task
def edit():
    l = task
    n = int(input("Enter the task number you want to Edit:\n"))
    keys = list(l.keys())
    values = list(l.values())
    while n not in range(1, len(keys) + 1):
        n = int(input("Enter a valid task number:\n"))
    l[input("Enter the task's new name:\n")] = values[n - 1]
    l.pop(keys[n - 1])


# Printing
def printing():
    l = task
    keys = list(l.keys())
    values = list(l.values())
    table.clear_rows()
    for i, j in zip(keys, values):
        table.add_row([keys.index(i) + 1, i, (math.floor(j * 15 / 100) * "#").ljust(16, " ") + f"{j}%"])
    print(table)


# Save
def save():
    l = task
    keys = list(l.keys())
    values = list(l.values())
    with open("Task Manager Keys.txt", "w") as file:
        file.seek(0)
        for i in keys:
            file.write(f"{i} ")
    with open("Task Manager Values.txt", "w") as file:
        file.seek(0)
        for i in values:
            file.write(f"{i} ")


# Read
def reading():
    l = task
    with open("Task Manager Keys.txt", "r") as file:
        for i in file.read().split():
            l[i] = ""
    keys = list(l.keys())
    with open("Task Manager Values.txt", "r") as file:
        for i, j in zip(file.read().split(), keys):
            l[j] = int(i)


# Start
while True:
    printing()
    k = int(input("1. Add\n2. Delete\n3. Update\n4. Edit\n5. Save\n6. Read\n0. Exit\n"))
    while k not in range(0, 8):
        k = int(input("Enter a valid number:\n"))
    if k == 1:
        adding()
    elif k == 2:
        deleting()
    elif k == 3:
        update()
    elif k == 4:
        edit()
    elif k == 5:
        save()
    elif k == 6:
        reading()
    # Exit
    else:
        save()
        break
