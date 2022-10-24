#!/bin/bash

# Check if Database is up and running before starting the service.
until nc -z "${DB_HOST}" "${DB_PORT}"; do
    echo "$(date) - waiting for database..."
    sleep 2
done

# Run Migrations
alembic upgrade head && alembic revision --autogenerate -m "latest revisions" && alembic upgrade head

# Run Service
uvicorn --host=0.0.0.0 --port=9559 --workers=10 --limit-concurrency=100 --backlog=100 --use-colors backend.router.api:app --reload