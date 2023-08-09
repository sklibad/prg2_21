from trip import *
from stop import *
from typing import Set, List


class StopSegment:
    def __init__(self, where_from, where_to):
        # Initialize the StopSegment instance with starting and ending Stop objects
        self.where_from: Stop = where_from
        self.where_to: Stop = where_to

        # List to store associated trips
        self.trips: List[Trip] = []

        # Set to store route short names
        self.route_short_names: Set[str] = set()

    def addTrip(self, trip: Trip):
        # Add a Trip instance to the list of associated trips
        self.trips.append(trip)

    def addRouteShortName(self, short_name: str):
        # Add a route short name to the set if it's not already present
        self.route_short_names.add(short_name)

    # Getters
    def getTripCount(self):
        # Return the number of associated trips
        return len(self.trips)

    def getRouteShortNames(self):
        # Return the set of route short names
        return self.route_short_names

    def getWhereFrom(self):
        # Return the starting Stop instance
        return self.where_from

    def getWhereTo(self):
        # Return the ending Stop instance
        return self.where_to