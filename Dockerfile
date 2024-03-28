# Use an official Python runtime as a parent image
FROM python:3.8.10

# Set the working directory in the container
WORKDIR /

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed dependencies specified in requirements.txt
RUN echo "Installing dependencies..."
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt
RUN python setup.py install

# Run your Python script when the container launches
CMD ["python", "pipeline/run_we.py"]
