class Route:
    def __init__(self, attributes):
        # Initialize instance variables with default values
        self.route_id = None
        self.agency_id = None
        self.route_short_name = None
        self.route_long_name = None
        self.route_type = None
        self.route_url = None
        self.route_color = None
        self.route_text_color = None
        self.is_night = None
        self.is_regional = None
        self.is_substitute_transport = None

        # If attributes are provided, load them into the instance
        if attributes is not None:
            self.loadAttributes(attributes)

    def loadAttributes(self, attributes: dict):
        # Load route attributes from the given dictionary

        if 'route_id' in attributes.keys():
            self.route_id = attributes['route_id']

        if 'agency_id' in attributes.keys():
            self.agency_id = attributes['agency_id']

        if 'route_short_name' in attributes.keys():
            self.route_short_name = attributes['route_short_name']

        if 'route_long_name' in attributes.keys():
            self.route_long_name = attributes['route_long_name']

        if 'route_type' in attributes.keys():
            self.route_type = attributes['route_type']

        if 'route_url' in attributes.keys():
            self.route_url = attributes['route_url']

        if 'route_color' in attributes.keys():
            self.route_color = attributes['route_color']

        if 'route_text_color' in attributes.keys():
            self.route_text_color = attributes['route_text_color']

        if 'is_night' in attributes.keys():
            self.is_night = attributes['is_night']

        if 'is_regional' in attributes.keys():
            self.is_regional = attributes['is_regional']

        if 'is_substitute_transport' in attributes.keys():
            self.is_substitute_transport = attributes['is_substitute_transport']

    # Getters
    def getID(self):
        # Return the route ID of the instance
        return self.route_id

    def getShortName(self):
        # Return the short name of the route
        return self.route_short_name
