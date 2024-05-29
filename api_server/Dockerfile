# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory in the container
WORKDIR /RabbiMQFlisolOpenSource

# Copy your script and any other necessary files into the container
COPY . /RabbiMQFlisolOpenSource

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run script.py when the container launches
CMD ["python", "send.py"]
