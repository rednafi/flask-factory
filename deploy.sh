#!/bin/bash

# add tags and container name
TAGNAME=flask_template
CONTAINERNAME=flask_template

# add option to run container in detached mode
DAEMON=$1

# stop running container
docker stop $CONTAINERNAME

# remove container
docker rm $CONTAINERNAME

# remove previous image
docker rmi $(docker images --format '{{.Repository}}:{{.Tag}}' | grep 'flask_demo')

# remove dangling images
sudo docker image prune -a --force

# build docker image
docker build . --tag=$TAGNAME

# run container from the built image
docker run $DAEMON -p 5000:5000 --name $CONTAINERNAME $TAGNAME
