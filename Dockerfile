FROM python:3.7.5-alpine


RUN mkdir /app
WORKDIR /app
COPY . /app
ENV FLASK_DEBUG 0
ENV FLASK_APP run.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN pip3 install -r requirements.txt
EXPOSE 5000

CMD ["flask", "run"]
