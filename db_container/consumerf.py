import pika, sys


# RabbitMQ message consumer function
def receive_tasks_from_rabbitmq(queue='functions'):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.17.0.2'))
    channel = connection.channel()
    channel.queue_declare(queue=queue, durable=True)

    try:
        # Set up consumer and start consuming
        channel.basic_consume(queue=queue, on_message_callback=process_task)
        channel.start_consuming()
    except KeyboardInterrupt:
        print("\nExiting...")
        # Additional cleanup or exit code can be added here if needed
        sys.exit(0)  # Exit gracefully with code 0
    finally:
        connection.close()


# Function to handle task processing
def process_task(ch, method, properties, body):
    # Decode the message
    message = body.decode('utf-8')
    
    # Check the message value and call appropriate function
    if message == '0':
        print("Received message 0. Performing func_0...")
        func_0()
    elif message == '1':
        print("Received message 1. Performing func_1...")
        func_1()
    else:
        print("Unknown message:", message)


def func_0():
    # TODO: when add tasks, update db, retrieve db and send to all clients rabbit queue
    pass


def func_1():
    # block_tasks