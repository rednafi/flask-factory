# Use slim buster images
FROM python:3.8.5-slim-buster

# Make a working directory
RUN mkdir /app
WORKDIR /app

# First, copy the requirements.txt only as it helps with caching
# Details: https://pythonspeed.com/articles/docker-caching-model/
COPY ./requirements.txt /app
RUN pip install -r requirements.txt

# Copy the source code
COPY . /app

# Turn of debugging in production
ENV FLASK_DEBUG 0

# Set entrypoint
ENV FLASK_APP flask_run.py
ENV FLASK_RUN_HOST 0.0.0.0
EXPOSE 4000

# Run Flask command
CMD ["gunicorn", "-b", "0.0.0.0:4000", "flask_run:application"]
