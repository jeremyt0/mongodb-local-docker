# Simple Mongodb local setup

You can either use a bash command or the docker compose yaml file to create a run mongo via docker.

## First things first

### Install docker

Mac
```
brew install docker
```

### Pull mongodb docker image

```
docker pull mongodb:7.0
```

*Can use any version you wish

### Nice to have

- [Docker Desktop GUI](https://www.docker.com/products/docker-desktop/)
- [MongoDB Compass GUI](https://www.mongodb.com/products/tools/compass)


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

Ensure you have `pymongo` installed as requirements.


## Additionals

Also install MongoDB Compass for the GUI to explore.

When the docker container is running, you can connect to `mongodb://localhost:12345/` as the URI.
