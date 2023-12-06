# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements-dev.txt

# Initialize the Reflex project
# Note: This assumes that reflex init can be run non-interactively
RUN reflex init

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Command to wait for the Postgres database to be ready before starting the app
# Install a PostgreSQL client to check for database readiness
RUN apt-get update && apt-get install -y postgresql-client

# Define a script to wait for Postgres
RUN echo "while ! pg_isready -h postgres -p 5432; do echo 'Waiting for Postgres...'; sleep 1; done;" > ./wait-for-postgres.sh
RUN chmod +x ./wait-for-postgres.sh

# Run the Reflex server when the container launches
CMD ["./wait-for-postgres.sh && reflex run"]
