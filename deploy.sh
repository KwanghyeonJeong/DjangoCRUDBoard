#!/bin/sh

REPOSITORY=/home/ubuntu/app

cd $REPOSITORY

sudo apt-get update \
  && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y docker-compose

nohup docker-compose down && docker-compose up --build > $REPOSITORY/nohup.out 2>&1 &