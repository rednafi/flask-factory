FROM python:3.7.5-alpine


RUN mkdir /app
WORKDIR /app
COPY . /app
ENV FLASK_DEBUG 0
ENV FLASK_APP run.py
RUN pip3 install -r requirements.txt
EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:application"]
