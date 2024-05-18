import sqlite3

table = input("Enter table name: ")
task_id = input("Enter task id: ")
unblocker_name = input("Enter your name: ")  # Assume the current user's name is provided

# Connect to the SQLite database
conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

def unblock_task(task_id, unblocker_name):
    try:
        # Retrieve the current blocker's name for the task
        cursor.execute(f"SELECT block_reason FROM {table} WHERE id = ?", (task_id,))
        current_blocker = cursor.fetchone()[0]

        # Check if the current user is the one who blocked the task
        if current_blocker == unblocker_name:
            # Update the 'blocked' column for the specified task
            cursor.execute(f"UPDATE {table} SET blocked = 0, block_reason = NULL WHERE id = ?", (task_id,))
            conn.commit()
            print(f"Task {task_id} unblocked successfully by {unblocker_name}.")
        else:
            print("You are not authorized to unblock this task.")

    except sqlite3.Error as e:
        print("Error unblocking task:", e)

unblock_task(task_id, unblocker_name)
