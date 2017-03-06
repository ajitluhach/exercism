import math


class Clock():

    def __init__(self, hour, minute):
        self.hour = 0
        self.minute = 0
        self._increment_minute(minute)
        self._increment_hour(hour)

    def add(self, mint):
        self._increment_minute(mint)
        return self

    def _increment_hour(self, hours):
        self.hour += hours
        self.hour = self.hour % 24

    def _increment_minute(self, minutes):
        self.minute = self.minute + minutes
        self._increment_hour(math.floor(self.minute//60))
        self.minute = self.minute % 60

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __str__(self):
        return "{:02}:{:02}".format(self.hour, self.minute)
