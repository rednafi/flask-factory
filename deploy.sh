#!/bin/bash
CONTAINER_NAME=flask-tmplt
TAG=flask
DAEMON=$1

sudo docker stop $CONTAINER_NAME
sudo docker rm $CONTAINER_NAME
sudo docker rmi $TAG 
sudo docker build . --tag=$TAG
sudo docker run $DAEMON -p 5000:5000 --name $CONTAINER_NAME $TAG 