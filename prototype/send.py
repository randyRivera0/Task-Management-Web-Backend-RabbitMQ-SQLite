import pika, sys
import Task

# Function to prompt user for task input
from Task import Task

# TODO: fetch the properties of the class automatically

def get_task_from_input():
    task_info = {}
    
    # Specify the properties you want to collect
    task_class_properties = ['id', 'name', 'importance', 'urgency', 'time', 'description', 'state', 'progress', 'blocked', 'block_reason']
    
    for prop in task_class_properties:
        task_info[prop] = input(f"Enter task {prop}: ")
    
    # Convert necessary properties to appropriate types
    task_info['time'] = int(task_info['time'])  # Assuming time is an integer
    task_info['progress'] = float(task_info['progress'])  # Assuming progress is a float
    
    # Convert 'blocked' attribute to a boolean
    task_info['blocked'] = task_info['blocked'].lower() in ['true', 'yes', '1']
    
    return Task(**task_info)


# Function to send task JSON via RabbitMQ
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

# Main loop
try:
    while True:
        department_name = input("Enter the department name: ")

        queue_name = department_name  

        # Prompt user for task input
        task = get_task_from_input()

        # Serialize task object to JSON
        task_json = task.to_json()

        # Send task JSON via RabbitMQ
        send_task_via_rabbitmq(task_json, queue_name)

except KeyboardInterrupt:
    print("\nExiting...")
    # Additional cleanup or exit code can be added here if needed
    sys.exit(0)  # Exit gracefully with code 0
