class StopTime:
    def __init__(self, attributes):
        # Initialize instance variables with default values
        self.trip_id = None
        self.arrival_time = None
        self.departure_time = None
        self.stop_id = None
        self.stop_sequence = None
        self.stop_headsign = None
        self.pickup_type = None
        self.drop_off_type = None
        self.continuous_pickup = None
        self.continuous_drop_off = None
        self.shape_dist_traveled = None
        self.timepoint = None
        self.trip_operation_type = None
        self.bikes_allowed = None

        # If attributes are provided, load them into the instance
        if attributes is not None:
            self.loadAttributes(attributes)

    def loadAttributes(self, attributes: dict):
        # Load stop time attributes from the given dictionary

        if 'trip_id' in attributes.keys():
            self.trip_id = attributes['trip_id']

        if 'arrival_time' in attributes.keys():
            self.arrival_time = attributes['arrival_time']

        if 'departure_time' in attributes.keys():
            self.departure_time = attributes['departure_time']

        if 'stop_id' in attributes.keys():
            self.stop_id = attributes['stop_id']

        if 'stop_sequence' in attributes.keys():
            self.stop_sequence = attributes['stop_sequence']

        if 'stop_headsign' in attributes.keys():
            self.stop_headsign = attributes['stop_headsign']

        if 'pickup_type' in attributes.keys():
            self.pickup_type = attributes['pickup_type']

        if 'drop_off_type' in attributes.keys():
            self.drop_off_type = attributes['drop_off_type']

        if 'continuous_pickup' in attributes.keys():
            self.continuous_pickup = attributes['continuous_pickup']

        if 'continuous_drop_off' in attributes.keys():
            self.continuous_drop_off = attributes['continuous_drop_off']

        if 'shape_dist_traveled' in attributes.keys():
            self.shape_dist_traveled = attributes['shape_dist_traveled']

        if 'timepoint' in attributes.keys():
            self.timepoint = attributes['timepoint']

        if 'trip_operation_type' in attributes.keys():
            self.trip_operation_type = attributes['trip_operation_type']

        if 'bikes_allowed' in attributes.keys():
            self.bikes_allowed = attributes['bikes_allowed']

    # Getters
    def getTripID(self):
        # Return the trip ID associated with the stop time
        return self.trip_id

    def getStopID(self):
        # Return the stop ID associated with the stop time
        return self.stop_id
    
