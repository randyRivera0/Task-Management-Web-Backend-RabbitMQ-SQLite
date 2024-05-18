import os
import datetime
import sqlite3
from importance_enum import Importance


def formula(duration, progress, deadline):
    day_format = "%d-%m-%Y"
    datetime_object = datetime.datetime.strptime(deadline, day_format)
    return (datetime_object - datetime.datetime.today()).total_seconds() / 3600 - (duration * (1 - progress))


# someone sends a message here for updating
# Connects to the db, fetch, sort, upload to redis, and publish to clients

# If it were a db, ORDER BY importance, time_range, add column time_range, and order db



# hours_left = duration (hrs) * (1 - progress (0-1))
# time_range = days_to_hours((deadline - time.day.today)) - hours_left
# Prioritize by time_range inside medium: lower values first (it means no time)


def rearrange_table2():
    # Get the current working directory
    cwd = os.getcwd()

    # Define the path to the database file relative to the current working directory
    db_path = os.path.join(cwd, 'prototype\\tasks.db')

    # Connect to the database
    conn = sqlite3.connect(db_path)
    conn.create_function("formula", 3, formula)

    c = conn.cursor()

    c.execute(f'''SELECT *,
        duration, progress, deadline, formula(duration, progress, deadline) AS time_range
        FROM finance
        ORDER BY importance DESC, time_range;
        ''')
    rows = c.fetchall()
    for row in rows:
        print(row)

    conn.commit()
    conn.close()


"""
def rearrange_table():
    # Connect to the database
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    
    # Create a new table with the desired ordering
    c.execute('''CREATE TABLE temp_table AS 
                 SELECT * FROM finance ORDER BY importance, time_range''')
    
    # Drop the original table
    c.execute('''DROP TABLE your_table''')
    
    # Rename the temporary table to the original table name
    c.execute('''ALTER TABLE temp_table RENAME TO your_table''')
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Call the function to rearrange the table
rearrange_table()


# Connect to the SQLite database
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Create a table with an 'importance' column
cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    task_name TEXT,
                    importance INTEGER
                )''')

# Function to convert enum to integer for storage
def enum_to_int(enum_val):
    return enum_val.value

# Function to convert integer to enum upon retrieval
def int_to_enum(int_val):
    return Importance(int_val)

# Insert a row with an enum value into the database
def insert_task_with_importance(task_name, importance):
    cursor.execute('INSERT INTO tasks (task_name, importance) VALUES (?, ?)', (task_name, enum_to_int(importance)))
    conn.commit()

# Retrieve a row from the database
def retrieve_task(task_id):
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    row = cursor.fetchone()
    if row:
        task_id, task_name, importance_int = row
        importance = int_to_enum(importance_int)
        return task_id, task_name, importance
    else:
        return None

# Example usage
insert_task_with_importance("Example Task", Importance.MEDIUM)
task_id, task_name, task_importance = retrieve_task(1)
print("Task ID:", task_id)
print("Task Name:", task_name)
print("Task Importance:", task_importance)

# Close the connection
conn.close()
"""

rearrange_table2()
