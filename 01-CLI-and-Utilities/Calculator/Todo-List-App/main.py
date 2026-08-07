import json
import os

FILENAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)


def show_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks found! Your list is empty.")
        return

    print("\n" + "=" * 40)
    print("📋 YOUR TO-DO LIST")
    print("=" * 40)
    for index, task in enumerate(tasks, start=1):
        status = "✅" if task["completed"] else "❌"
        print(f"{index}. [{status}] {task['title']}")
    print("=" * 40)


def add_task(tasks):
    title = input("\nEnter task description: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        save_tasks(tasks)
        print(f"✨ Task added: '{title}'")
    else:
        print("⚠️ Task description cannot be empty.")


def mark_completed(tasks):
    show_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(
            input("\nEnter task number to mark as completed: ")
        )
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            save_tasks(tasks)
            print(
                f"🎉 Task {task_num} marked as completed!"
            )
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")


def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("\nEnter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"🗑️ Deleted task: '{removed['title']}'")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n--- 📌 TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("\n👋 Goodbye! Happy coding!")
            break
        else:
            print("⚠️ Invalid choice! Please select between 1 and 5.")


if __name__ == "__main__":
    main()