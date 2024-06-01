from flask import Flask, request, jsonify
from flask_cors import CORS
from Task import Task  # Assuming Task class is defined in Task.py
import pika, sys
import Task  # Import the Task class from task.py

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


tasks = []

# Route to add a new video task
@app.route('/obtener', methods=['GET'])
def obtener_tareas():
    receive_tasks_from_rabbitmq()
    return tasks


def receive_tasks_from_rabbitmq(department='client'):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=department, durable=True)

    try:
        # Set up consumer and start consuming
        channel.basic_consume(queue=department, on_message_callback=process_tasks)
        channel.start_consuming()
        
    except KeyboardInterrupt:
        print("\nExiting...")
        # Additional cleanup or exit code can be added here if needed
        sys.exit(0)  # Exit gracefully with code 0
    finally:
        connection.close()
    

def tasks_to_string(tasks):
    """
    Convert a list of task dictionaries into a single string.
    
    Args:
    - tasks (list): List of task dictionaries
    
    Returns:
    - task_string (str): String representation of tasks
    """
    task_string = ""
    for task in tasks:
        task_string += f"Name: {task['name']}, Description: {task['description']}, Importance: {task['importance']}, Progress: {task['progress']}, Duration: {task['duration']}, Deadline: {task['deadline']}, Blocked: {task['blocked']}, Blocked by: {task['blocked_by']}, Block reason: {task['block_reason']}\n"
    return task_string


def process_tasks(channel, method, properties, body):
    """
    Split a long string of tasks into individual task strings.
    
    Args:
    - task_string (str): Long string of task representations
    
    Returns:
    - tasks (list): List of task strings
    """
    # global tasks
    received_tasks = body.strip().split('\n')
    tasks.extend(received_tasks)  # Append received tasks to global variable
    channel.basic_ack(delivery_tag=method.delivery_tag)  
    

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)