import datetime
from django.test import TestCase
from djtweetar.runlogs.models import *

class RunLogTest(TestCase):
    def test_elapsed(self):
        noon = datetime.datetime(2010, 10, 1, 12)
        later = datetime.datetime(2010, 10, 1, 12, 0, 55)

        tr = TweetarRun.objects.create(begin=noon, end=later, total_stations=2, stations_updated=2, station_exceptions=0)

        self.assertEqual(tr.elapsed_seconds, 55)
