FILENAME = "tasks.txt"


# ---------- File Handling ----------

def load_tasks():
    tasks = []  # this will be a list of dictionaries

    try:
        file = open(FILENAME, "r")
    except FileNotFoundError:
        return tasks  # no file yet, so return an empty list

    for line in file:
        line = line.strip()  # removes the newline character at the end
        if line == "":
            continue

        # each line in the file looks like: done|Buy groceries
        status, title = line.split("|", 1)

        task = {
            "title": title,
            "done": status == "1"
        }
        tasks.append(task)

    file.close()
    return tasks


def save_tasks(tasks):
    file = open(FILENAME, "w")

    for task in tasks:
        status = "1" if task["done"] else "0"
        file.write(status + "|" + task["title"] + "\n")

    file.close()


# ---------- Core Features ----------

def add_task(tasks):
    title = input("Enter the task: ")

    task = {
        "title": title,
        "done": False
    }
    tasks.append(task)
    print("Task added.")


def view_tasks(tasks):
    if len(tasks) == 0:
        print("\nYour to-do list is empty.")
        return

    print("\n--- Your Tasks ---")
    index = 1
    for task in tasks:
        if task["done"]:
            status = "[x]"
        else:
            status = "[ ]"
        print(str(index) + ". " + status + " " + task["title"])
        index += 1


def mark_done(tasks):
    view_tasks(tasks)
    if len(tasks) == 0:
        return

    number = int(input("Enter the task number to mark as done: "))

    if number < 1 or number > len(tasks):
        print("Invalid task number.")
        return

    tasks[number - 1]["done"] = True
    print("Task marked as done.")


def delete_task(tasks):
    view_tasks(tasks)
    if len(tasks) == 0:
        return

    number = int(input("Enter the task number to delete: "))

    if number < 1 or number > len(tasks):
        print("Invalid task number.")
        return

    removed = tasks.pop(number - 1)
    print("Deleted: " + removed["title"])


# ---------- Menu ----------

def show_menu():
    print("\n=== To-Do List App ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()