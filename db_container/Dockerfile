# Use a base image that includes the necessary dependencies
FROM python:3.9

# Install SQLite
RUN apt-get update && apt-get install -y sqlite3

# Set the working directory in the container
WORKDIR /RabbiMQFlisolOpenSource

# Copy your script and any other necessary files into the container
COPY . /RabbiMQFlisolOpenSource

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "consumer.py"]
