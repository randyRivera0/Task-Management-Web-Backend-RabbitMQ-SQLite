import sqlite3, utils

table = input("Enter table name: ")
task_id = input("Enter task id: ")
blocker_name = input("Enter your name: ")  # Assume the name of the person blocking the task is provided

# Connect to the SQLite database
conn = utils.connect_to_db()
cursor = conn.cursor()

def block_task(task_id, blocker_name):
    try:
        # Update the 'blocked' column and 'block_reason' for the specified task
        cursor.execute(f"UPDATE {table} SET blocked = 1, block_reason = ? WHERE id = ?", (blocker_name, task_id,))
        conn.commit()
        print(f"Task {task_id} blocked successfully by {blocker_name}.")
    except sqlite3.Error as e:
        print("Error blocking task:", e)

block_task(task_id, blocker_name)
