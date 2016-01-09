# EventstoreProjectionsCollector

## dependencies

Make sure you have python and diamond installed

## running diamond

Running diamond with the EventStoreProjectionsCollector in debug mode.
A very basic diamond config is used for easy debugging of the collector. 
All paths are relative to the project root.

```
diamond --foreground  --log-stdout --skip-pidfile -c ./config/diamond.conf
```

## todo

adding tests! 
adding example output


## example output is:
```
servers.erlkoenig.eventstore.projections.participations-per-person.eventsProcessedAfterRestart 10 1452366154
servers.erlkoenig.eventstore.projections.participations-per-person.bufferedEvents 0 1452366154
servers.erlkoenig.eventstore.projections.participations-per-person.coreProcessingTime 2 1452366154
servers.erlkoenig.eventstore.projections.participations-per-person.epoch -1 1452366154
servers.erlkoenig.eventstore.projections.participations-per-person.version 1 1452366154
servers.erlkoenig.eventstore.projections.participations-per-person.progress 100 1452366154
servers.erlkoenig.eventstore.projections.participations-per-person.status 1 1452366154
servers.erlkoenig.eventstore.projections.participations-per-person.writePendingEventsBeforeCheckpoint 0 1452366154
servers.erlkoenig.eventstore.projections.participations-per-person.partitionsCached 7 1452366154
servers.erlkoenig.eventstore.projections.participations-per-person.writesInProgress 0 1452366154
servers.erlkoenig.eventstore.projections.participations-per-person.readsInProgress 0 1452366154
servers.erlkoenig.eventstore.projections.participations-per-person.writePendingEventsAfterCheckpoint 0 1452366154
```