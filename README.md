# EventstoreProjectionsCollector


## build the docker container

```
cd docker; docker build -t quay.io/psybizz/eventstoreprojections .
```

## run the docker container

docker run --name eventstoreprojections  -d  -t quay.io/psybizz/eventstoreprojections diamond --foreground  --log-stdout --skip-pidfile