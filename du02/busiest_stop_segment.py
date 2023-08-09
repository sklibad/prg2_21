import csv
from stop import *
from stoptime import *
from trip import *
from routes import *
from stopsegment import *
import os

# Initialize dictionaries for each class
stops = {}
stop_times = {}
trips = {}
routes = {}
stop_segments = {}

# Get the absolute path of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load stops to dictionary by primary key = stop_id, item = Stop object
with open(os.path.join(current_dir, 'gtfs/stops.txt'), newline='', encoding="utf-8") as data_csv:
    reader = csv.DictReader(data_csv, delimiter=',')
    for row in reader:
        stop = Stop(row)
        stops[stop.getID()] = stop

# Load routes to dictionary by primary key = route_id, item = Route object
with open(os.path.join(current_dir, 'gtfs/routes.txt'), newline='', encoding="utf-8") as data_csv:
    reader = csv.DictReader(data_csv, delimiter=',')
    for row in reader:
        route = Route(row)
        routes[route.getID()] = route

# Load stop times to dictionary by foreign key = trip_id, item = StopTime object
with open(os.path.join(current_dir, 'gtfs/stop_times.txt'), newline='', encoding="utf-8") as data_csv:
    reader = csv.DictReader(data_csv, delimiter=',')
    reader = list(reader)
    reader = sorted(reader, key=lambda x: x['trip_id'])
    trip_id = ""
    for row in reader:
        stop_time = StopTime(row)
        if stop_time.getTripID() == trip_id:
            bus_line_stops.append(stop_time)
        else:
            if trip_id != "":
                stop_times[trip_id] = bus_line_stops
            # Foreign key
            trip_id = stop_time.getTripID()
            bus_line_stops = [stop_time]
    stop_times[trip_id] = bus_line_stops

# Load trips to dictionary by foreign key = route_id, item = Trip object
with open(os.path.join(current_dir, 'gtfs/trips.txt'), newline='', encoding="utf-8") as data_csv:
    reader = csv.DictReader(data_csv, delimiter=',')
    reader = list(reader)
    reader = sorted(reader, key=lambda x: x['route_id'])
    route_id = ""
    for row in reader:
        trip = Trip(row)
        if trip.getRouteID() == route_id:
            route_trips.append(trip)
        else:
            if route_id != "":
                trips[route_id] = route_trips
            # Foreign key
            route_id = trip.getRouteID()
            route_trips = [trip]
    trips[route_id] = route_trips


# Browse all routes
for route_ID, route in routes.items():

    # Route name (number code)
    route_name = route.getShortName()

    # List of trips on the route
    route_trips = trips[route_ID]

    # Browse all those trips
    for trip in route_trips:

        # Trip ID
        trip_ID = trip.getID()

        # List of stop times (stops) of the trip
        stop_time = stop_times[trip_ID]

        # Browse all stop times
        for i in range(len(stop_time) - 1):
            
            # ID of previous stop
            where_from = stop_time[i].getStopID()
            from_stop_instance = stops[where_from]

            # ID of next stop
            where_to = stop_time[i+1].getStopID()
            to_stop_instance = stops[where_to]

            # Try if current segment already exists
            if (from_stop_instance, to_stop_instance) in stop_segments.keys():
                # Existing stop segment
                ss = stop_segments[(from_stop_instance, to_stop_instance)]

                # Add trip to segment
                ss.addTrip(trip)

                # Add route name to segment
                ss.addRouteShortName(route_name)

            else:
                # Create stop segment
                ss = StopSegment(from_stop_instance, to_stop_instance)

                # Add trip to segment
                ss.addTrip(trip)

                # Add route name to segment
                ss.addRouteShortName(route_name)

                # Add new stop segment into list of stop segments
                stop_segments[(from_stop_instance, to_stop_instance)] = ss


# Dictionary where key = stop_segment_ID, item = number of trips
segment_trip_count = {}

# Sort dictionary by values
sorted_segments = sorted(stop_segments.items(), key=lambda kv: kv[1].getTripCount(), reverse=True)

# Browse 5 busiest stop segments
for segment in sorted_segments[0:5]:
    stop_segment = stop_segments[segment[0]]

    # Start stop name
    from_stop = stops[segment[0][0].getID()].getName()

    # End stop name
    to_stop = stops[segment[0][1].getID()].getName()

    # Route names
    route_names = stop_segments[segment[0]].getRouteShortNames()

    # Print result
    print(from_stop, "-", to_stop, "(" + str(segment[1].getTripCount()) + ")", route_names)

