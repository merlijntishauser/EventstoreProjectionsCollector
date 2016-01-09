# coding=utf-8

"""
A Simple collector which calls the Evenstore API for the status of projections and
parses this to flat metrics.
String values are ignored, except for the Key "status". This key can have two values:

    Running -> cast to 1
    Stopped -> cast to 0

The name of the projections are used in the metrics path.

This collector is based upon the HTTPJSONCollector.

#### Dependencies

 * urllib2

"""

import urllib2
import json
import diamond.collector


class EventstoreProjectionsCollector(diamond.collector.Collector):

    def get_default_config_help(self):
        config_help = super(EventstoreProjectionsCollector, self).get_default_config_help()
        config_help.update({
            'url': 'Full URL',
            'headers': 'Header variable if needed. '
            'Will be added to every request',
        })
        return config_help

    def get_default_config(self):
        default_config = super(EventstoreProjectionsCollector, self).get_default_config()
        default_config.update({
            'path': 'eventstore',
            'url': 'http://localhost/stat',
            'headers': {'User-Agent': 'Diamond Eventstore Projections metrics collector'},
        })
        return default_config

    def _json_to_flat_metrics(self, prefix, data):

        for key, value in data.items():
            if isinstance(value, dict):
                for k, v in self._json_to_flat_metrics(
                        "%s.%s" % (prefix, key), value):
                    yield k, v
            elif isinstance(value, basestring):
                if value == "Running":
                    value = 1
                    yield ("%s.%s" % (prefix, key), value)
                elif value == "Stopped":
                    value = 0
                    yield ("%s.%s" % (prefix, key), value)
                else:
                    self.log.debug("ignoring string value = %s", value)
            else:
                try:
                    int(value)
                except ValueError:
                    self.log.debug("typecasting to int failed, value = %s", value)
                finally:
                    yield ("%s.%s" % (prefix, key), value)

    def collect(self):
        url = self.config['url']

        req = urllib2.Request(url, headers=self.config['headers'])
        req.add_header('Content-type', 'application/json')

        try:
            resp = urllib2.urlopen(req)
        except urllib2.URLError as e:
            self.log.error("Can't open url %s. %s", url, e)
        else:
            content = resp.read()
            try:
                json_dict = json.loads(content)
                projections = json_dict['projections']

                data = {}
                for projection in projections:
                    data[projection["name"]] = projection
            except ValueError as e:
                self.log.error("Can't parse JSON object from %s. %s", url, e)
            else:
                for metric_name, metric_value in self._json_to_flat_metrics(
                        "projections", data):
                    self.publish(metric_name, metric_value)
