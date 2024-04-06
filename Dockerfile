# Use an official Python runtime as a parent image
FROM python:3.10.9

# Set the working directory in the container
WORKDIR /

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed dependencies specified in requirements.txt
RUN echo "Installing dependencies..."
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN python setup.py install

# Run your Python script to calc elos tables
RUN python tennis_elo/pipeline/run_elo_v2.py

# Expose port 8000 (or any other port your FastAPI application listens on)
EXPOSE 8000

# Command to run the FastAPI application using uvicorn with auto-reload
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
