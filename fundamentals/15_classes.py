# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
    """
    Instance that takes lat and lon
    """
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    """
    add name to LatLon class
    """
    def __init__(self, name, lat, lon):
        self.name = name
        super().__init__(lat=lat, lon=lon)

    def __str__(self):
        return 'Name: ' + self.name + ',' +' latitude: '+ str(self.lat) + ',' + ' longitude: '+ str(self.lon)


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    """
    add difficulty and size
    """
    def __init__(self, difficulty, size, name, lat, lon):
        self.difficulty = difficulty
        self.size = size
        super().__init__(name, lat, lon)

    def __str__(self):
        return 'Name: ' + self.name + ',' +' latitude: '+ str(self.lat) + ',' + \
            ' longitude: '+ str(self.lon) + ', difficulty: ' + str(self.difficulty) \
                + ', size: ' + str(self.size)


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = Waypoint(name="Catacombs", lat=41.70505, lon=-121.51521)
print(waypoint.name, waypoint.lat, waypoint.lon)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = Geocache(
    name="Newberry View", difficulty=1.5, size=2, lat=44.052137, lon=-121.41556
    )

# Print it--also make this print more nicely
print(geocache)
