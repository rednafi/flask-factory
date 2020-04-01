FROM python:3.8.2-slim-buster


RUN mkdir /app
WORKDIR /app
COPY . /app
ENV FLASK_DEBUG 0
ENV FLASK_APP flask_run.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN pip3 install -r requirements.txt
EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "flask_run:application"]
