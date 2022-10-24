FROM python:3.10.0-slim

# install dev dependencies
RUN apt-get update -y && \
    apt-get install -y python3-dev gcc && \
    apt-get update && apt-get -y install netcat && apt-get clean

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/app/backend/"

# copy project
COPY ./backend ./backend
COPY run.sh ./

# copy migration configs
COPY ./alembic.ini ./
COPY ./alembic ./alembic

RUN pip install --upgrade pip && \
    pip install -r ./backend/requirements.txt

EXPOSE 9559

RUN chmod +x ./run.sh
CMD ["./run.sh"]