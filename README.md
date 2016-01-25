# EventstoreProjectionsCollector

This collector polls an Eventstore for the status of projections and parses this to flat metrics.
String values are ignored, except for the name and status. 
Name is used for the metric path, status is translated to an integer (running = 1, stopped = 0).
Note: "$" are replaced by underscores (_) in the projection name to avoid problems with grafana.

Be aware the author is a python n00b and it's only tested against a single node eventstore. 

Url to be polled should look like: http://hostname:2113/projections/all-non-transient

## Dependencies

Make sure you have python and diamond installed

## Running diamond

Running diamond with the EventStoreProjectionsCollector in debug mode.
A very basic diamond config is used for easy debugging of the collector. 
All paths are relative to the project root.

```
diamond --foreground  --log-stdout --skip-pidfile -c ./config/diamond.conf
```

## Todo

[X] add unittests
[ ] improve unittests (split existing single test into multiple specific tests)
[ ] add testrunner script
[ ] add pep8 setup/ini

## Developer hints
This repository can be used to develop "stand alone" the collector. The code should be copied manually to the python-diamond/Diamond repository.
You can copy the src/eventstore directory to src/collectors/eventstore.

From the root of the project you can run the unittests:

```
python test.py 
```

And quality control tools:

```
pep8 --config=.pep8 src bin/diamond bin/diamond-setup build_doc.py setup.py test.py
```

You will need to have pep8 and mock installed by running:
```
pip install mock pep8
```

## Example output
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