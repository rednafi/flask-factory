FROM python:3.7.4-alpine3.10

RUN mkdir /app
COPY . /app
WORKDIR /app

ENV FLASK_DEBUG 1
ENV FLASK_APP run_flask.py
RUN pip install -r requirements.txt


# Expose is NOT supported by Heroku
EXPOSE 5000 		

# Run the image as a non-root user
# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku			
#CMD gunicorn --bind 0.0.0.0:$PORT wsgi 

CMD ["python", "./flask-ascii-art/run_flask.py"]
