#!/bin/bash

SOURCE_IMAGE="bhuvana20/fitness-tracker:v1"
TARGET_IMAGE="bhuvana20/fitness-tracker:prod"

LOG_FILE="promotion.log"

echo "Starting Promotion..." | tee -a $LOG_FILE

docker pull $SOURCE_IMAGE

if [ $? -ne 0 ]; then
  echo "Image Pull Failed" | tee -a $LOG_FILE
  exit 1
fi

docker tag $SOURCE_IMAGE $TARGET_IMAGE

docker push $TARGET_IMAGE

echo "Promotion Successful" | tee -a $LOG_FILE
