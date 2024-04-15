# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install cron and set up the log file
RUN apt-get update && apt-get -y install cron
RUN touch /var/log/cron.log

# Add crontab file in the cron directory
ADD crontab /etc/cron.d/time-entry-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/time-entry-cron

# Apply cron job
RUN crontab /etc/cron.d/time-entry-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log