import json, sys, pika, time, sqlite3
import Task  # Import the Task class from task.py

# Function to process received task
def process_task(channel, method, properties, body):
    # Deserialize JSON string to task object
    task_data = json.loads(body)
    print(task_data)
    task = Task.Task(**task_data)

    # Store task in the database
    store_task_in_database(task)

    # TODO: After task or after db ack?
    channel.basic_ack(delivery_tag=method.delivery_tag)


# Adjusted store_task_in_database function
def store_task_in_database(task):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('tasks.db')
        print("Connection with the DataBase successful")
        c = conn.cursor()

        # Convert state and blocked to integers
        blocked = 1 if task.blocked else 0

        # Insert task data into the database
        c.execute("INSERT INTO tasks (id, name, importance, urgency, time, description, state, progress, blocked, block_reason) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                  (task.id, task.name, task.importance, task.urgency, task.time, task.description, task.state, task.progress, blocked, task.block_reason))
        time.sleep(1)

        # Commit changes and close connection
        conn.commit()
        conn.close()
        print("Task inserted successfully")
    except Exception as e:
        print("Error occurred while inserting task:", e)




# RabbitMQ message consumer function
def receive_tasks_from_rabbitmq(department, importance_queue):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=importance_queue, durable=True)

    try:
        # Set up consumer and start consuming
        channel.basic_consume(queue=importance_queue, on_message_callback=process_task)
        channel.start_consuming()
    except KeyboardInterrupt:
        print("\nExiting...")
        # Additional cleanup or exit code can be added here if needed
        sys.exit(0)  # Exit gracefully with code 0
    finally:
        connection.close()

# Create a table to store tasks in the SQLite database
def create_database_schema():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    # Create table if not exists
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY, name TEXT, importance TEXT, urgency TEXT, time INTEGER, description TEXT, state TEXT, progress REAL, blocked INTEGER, block_reason TEXT)''')

    conn.commit()
    conn.close()

# Create database schema if not exists
create_database_schema()

# Prompt user for the department name
department = input("Enter the department name: ")

importance_queue = department

# Loop indefinitely
while True:
        # Buffer message indicating the program is running
        print("Program is running. Press Ctrl+C to exit.")
        receive_tasks_from_rabbitmq(department, importance_queue)
        time.sleep(1)  # Wait for 1 seconds before checking again
                