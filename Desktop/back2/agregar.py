from flask import Flask, request, jsonify
from flask_cors import CORS
from Task import Task  # Assuming Task class is defined in Task.py
import pika

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


# Connection parameters for RabbitMQ
RABBITMQ_HOST = 'localhost'
RABBITMQ_PORT = 5672
RABBITMQ_QUEUE = 'tasks'

# Establishing connection to RabbitMQ
# connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT))
# channel = connection.channel()
# channel.queue_declare(queue=RABBITMQ_QUEUE)

# add put reload
# ordenar
# add obtain and get, 

# Route to add a new video task
@app.route('/agregar', methods=['POST'])
def agregar_tarea():
    tarea_data = request.json  # Assuming the request contains JSON data representing the task
    
    # Print the received JSON string for debugging
    print("Received JSON Data:", tarea_data)

    tarea = Task(**tarea_data)  # Creating Task object from JSON data

    message = tarea.to_json()


    # Publish message to RabbitMQ queue
    # channel.basic_publish(exchange='', routing_key=RABBITMQ_QUEUE, body=message)

    # Send task JSON via RabbitMQ
    send_task_via_rabbitmq(message, 'tasks')

    return jsonify({'message': 'Tarea agregada exitosamente'}), 201


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


if __name__ == '__main__':
    app.run(debug=True)
