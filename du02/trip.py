class Trip:
    def __init__(self, attributes):
        # Initialize instance variables with default values
        self.route_id = None
        self.service_id = None
        self.trip_id = None
        self.trip_headsign = None
        self.trip_short_name = None
        self.direction_id = None
        self.block_id = None
        self.shape_id = None
        self.wheelchair_accessible = None
        self.bikes_allowed = None
        self.exceptional = None

        # If attributes are provided, load them into the instance
        if attributes is not None:
            self.loadAttributes(attributes)

    def loadAttributes(self, attributes: dict):
        # Load trip attributes from the given dictionary

        if 'route_id' in attributes.keys():
            self.route_id = attributes['route_id']

        if 'service_id' in attributes.keys():
            self.service_id = attributes['service_id']

        if 'trip_id' in attributes.keys():
            self.trip_id = attributes['trip_id']

        if 'trip_headsign' in attributes.keys():
            self.trip_headsign = attributes['trip_headsign']

        if 'trip_short_name' in attributes.keys():
            self.trip_short_name = attributes['trip_short_name']

        if 'direction_id' in attributes.keys():
            self.direction_id = attributes['direction_id']

        if 'block_id' in attributes.keys():
            self.block_id = attributes['block_id']

        if 'shape_id' in attributes.keys():
            self.shape_id = attributes['shape_id']

        if 'wheelchair_accessible' in attributes.keys():
            self.wheelchair_accessible = attributes['wheelchair_accessible']

        if 'bikes_allowed' in attributes.keys():
            self.bikes_allowed = attributes['bikes_allowed']

        if 'exceptional' in attributes.keys():
            self.exceptional = attributes['exceptional']

    def getID(self):
        # Return the trip ID of the instance
        return self.trip_id

    def getRouteID(self):
        # Return the route ID associated with the trip
        return self.route_id
