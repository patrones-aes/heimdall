#!/bin/sh

while ! nc -z $DATABASE_HOST $DATABASE_PORT ; do
    echo "Waiting for database connection"
    sleep 3
done

uvicorn src.main:app --host $APP_HOST --port $APP_PORT
