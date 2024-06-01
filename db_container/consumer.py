import os
import sys

# Add the parent directory of the utils module to Python's module search path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

# Now you should be able to import the utils module
import utils

import json, pika, time, sqlite3, utils
import Task  # Import the Task class from task.py


# Adjusted store_task_in_database function
def store_task_in_database(department, task):
    try:
        conn = utils.connect_to_db()
        print("Connection with the DataBase successful")
        c = conn.cursor()

        # Convert state and blocked to integers
        blocked = 1 if task.blocked else 0

        # Create table if not exists
        c.execute(f'''CREATE TABLE IF NOT EXISTS {department}
                 (id INTEGER PRIMARY KEY, name TEXT, description TEXT, deadline TEXT, importance TEXT, duration INTEGER, progress REAL, state TEXT, blocked INTEGER, block_reason TEXT)''')


        # Insert task data into the database
        c.execute(f"INSERT INTO {department} (id, name, description, deadline, importance, duration, progress, state, blocked, block_reason) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                  (task.id, task.name, task.description, task.deadline, task.importance, task.duration, task.progress, task.state, task.blocked, task.block_reason))
        time.sleep(1)

        # Commit changes and close connection
        conn.commit()
        conn.close()
        print("Task inserted successfully")
    except Exception as e:
        print("Error occurred while inserting task:", e)

def obtain_tasks(db='tasks.db'):
    # Connect to the SQLite database
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    try:
        # Execute a SELECT query to retrieve all tasks
        cursor.execute("SELECT * FROM tasks")
        
        # Fetch all rows from the result set
        tasks = cursor.fetchall()
        # Convert tasks tuples to a big string
        tasks_string = "\n".join(map(str, tasks))
        return tasks_string
    except sqlite3.Error as e:
        print("Error retrieving tasks:", e)
        return None
    finally:
        # Close the database connection
        conn.close()



def send_task_via_rabbitmq(task_json, queue_name):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_publish(exchange='',
                          routing_key=queue_name,
                          body=task_json,
                          properties=pika.BasicProperties(
                              delivery_mode=2,  # make message persistent
                          ))
    print("Task sent to RabbitMQ")
    connection.close()   


def send_clients():
    tasks_strings = obtain_tasks()
    send_task_via_rabbitmq(tasks_strings)


# Function to process received task
def process_task(channel, method, properties, body):
    # Deserialize JSON string to task object
    task_data = json.loads(body)
    print(task_data)
    task = Task.Task(**task_data)

    # Store task in the database
    store_task_in_database(department, task)

    send_clients()

    # TODO: After task or after db ack?
    channel.basic_ack(delivery_tag=method.delivery_tag)


# RabbitMQ message consumer function
def receive_tasks_from_rabbitmq(department):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.17.0.2'))
    channel = connection.channel()
    channel.queue_declare(queue=department, durable=True)

    try:
        # Set up consumer and start consuming
        channel.basic_consume(queue=department, on_message_callback=process_task)
        channel.start_consuming()
    except KeyboardInterrupt:
        print("\nExiting...")
        # Additional cleanup or exit code can be added here if needed
        sys.exit(0)  # Exit gracefully with code 0
    finally:
        connection.close()

# Create a table to store tasks in the SQLite database
def create_database_schema():
     # Get the current working directory
    cwd = os.getcwd()

    # Define the path to the database file relative to the current working directory
    db_path = os.path.join(cwd, 'prototype\\tasks.db')
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Create table if not exists
    c.execute('''CREATE TABLE IF NOT EXISTS finance
                 (id INTEGER PRIMARY KEY, name TEXT, description TEXT, deadline TEXT, importance TEXT, duration INTEGER, progress REAL, state TEXT, blocked INTEGER, block_reason TEXT)''')

    conn.commit()
    conn.close()

# Create database schema if not exists
create_database_schema()

# Prompt user for the department name
department = input("Enter the department name: ")


# Loop indefinitely
while True:
        # Buffer message indicating the program is running
        print("Program is running. Press Ctrl+C to exit.")
        receive_tasks_from_rabbitmq(department)
        time.sleep(1)  # Wait for 1 seconds before checking again         
