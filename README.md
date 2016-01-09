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
