# Simple Mongodb local setup

You can either use a bash command or the docker compose yaml file to create a run mongo via docker.

## Bash

```
docker run -d --name mongo-demo -p 12345:27017 -v mongodemo:/data/db mongo:7.0
```

## Using docker-compose

Change directory to current directory `~/.../mongodb-local-docker`

```
cd mongodb-local-docker
docker compose up
```

## Running python

Run the python `main.py` to confirm that the connection works.


## Additionals

Also install MongoDB Compass for the GUI to explore.

When the docker container is running, you can connect to `mongodb://localhost:12345/` as the URI.
