FROM python:3.9

# Install required Python packages
RUN pip install --no-cache-dir Flask opencv-python-headless tensorflow numpy

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "server.py"]
