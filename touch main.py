import csv
import os
from datetime import datetime

if not os.path.exists("tasks.csv"):
    with open("tasks.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Due Date", "Priority", "Status"])

def add_task():
    task = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (High/Medium/Low): ")
    status = "Pending"

    task_id = str(int(datetime.now().timestamp()))  # unique ID

    with open("tasks.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([task_id, task, due_date, priority, status])
    
    print("✅ Task added!\n")

def view_tasks():
    print("\n📝 To-Do List:\n")
    with open("tasks.csv", mode='r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == 0:
                print(f"{row[0]:<12} | {row[1]:<30} | {row[2]:<12} | {row[3]:<8} | {row[4]}")
                print("-" * 80)
            else:
                print(f"{row[0]:<12} | {row[1]:<30} | {row[2]:<12} | {row[3]:<8} | {row[4]}")

def mark_complete():
    task_id = input("Enter the ID of the task to mark as completed: ")
    tasks = []

    with open("tasks.csv", mode='r') as file:
        reader = csv.reader(file)
        tasks = list(reader)

    updated = False
    for row in tasks[1:]:  # Skip header
        if row[0] == task_id:
            row[4] = "Completed"
            updated = True

    if updated:
        with open("tasks.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(tasks)
        print("✅ Task marked as completed.")
    else:
        print("⚠️ Task ID not found.")

def delete_task():
    task_id = input("Enter the ID of the task to delete: ")
    tasks = []

    with open("tasks.csv", mode='r') as file:
        reader = csv.reader(file)
        tasks = list(reader)

    original_len = len(tasks)
    tasks = [row for row in tasks if row[0] != task_id or row[0] == "ID"]

    if len(tasks) < original_len:
        with open("tasks.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(tasks)
        print("🗑️ Task deleted.")
    else:
        print("⚠️ Task ID not found.")


import pandas as pd

def export_to_excel():
    try:
        df = pd.read_csv("tasks.csv")
        df.to_excel("tasks.xlsx", index=False)
        print("✅ Exported to tasks.xlsx")
    except Exception as e:
        print("❌ Export failed:", e)

def menu():
    while True:
        print("\n=== 🧠 To-Do List Manager ===")
        print("1. ➕ Add Task")
        print("2. 📋 View Tasks")
        print("3. ✅ Mark Task as Completed")
        print("4. 🗑️ Delete Task")
        print("5. 📤 Export to Excel")
        print("6. ❌ Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            export_to_excel()
        elif choice == '6':
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
