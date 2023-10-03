""" soteriareitti/utils/geo.py """
import math


class Location:
    """Location class represents a location on the map
    """

    def __init__(self, latitude: float, longitude: float):
        """ 
        Initialize a location with latitude and longitude
        Latitude and longitude are in degrees
        """
        if not isinstance(latitude, float) or not isinstance(longitude, float):
            raise TypeError(
                f"Latitude and longitude must be floats,"
                f"not {type(latitude)} and {type(longitude)}")

        self.longitude = longitude
        self.latitude = latitude

    @classmethod
    def from_str(cls, location_str: str) -> "Location":
        lat_str, lon_str = location_str.strip("(").strip(")").split(",")
        return cls(float(lat_str), float(lon_str))

    def __str__(self):
        return f"({self.latitude},{self.longitude})"

    def __repr__(self):
        return f"<soteriareitti.Location ({self.latitude}, {self.longitude})>"

    def __eq__(self, other: "Location" or tuple) -> bool:
        if isinstance(other, Location):
            return self.longitude == other.longitude and self.latitude == other.latitude
        if isinstance(other, tuple):
            return self.longitude == other[0] and self.latitude == other[1]
        return False

    def as_tuple(self) -> tuple[float, float]:
        return (self.latitude, self.longitude)

    def rounded(self, precision: int = 4) -> "Location":
        """ Return location rounded to given precision """
        return Location(round(self.latitude, precision), round(self.longitude, precision))

    @property
    def latitude_rad(self) -> float:
        """ Return latitude in radians """
        return math.radians(self.latitude)

    @property
    def longitude_rad(self) -> float:
        """ Return longitude in radians """
        return math.radians(self.longitude)


class Distance:
    """ Distance class represents a distance on the map"""

    def __init__(self, distance_meters: float):
        self.meters = distance_meters

    def __repr__(self):
        return f"<soteriareitti.Distance meters={self.meters}>"

    def __eq__(self, distance: "Distance" or float | int) -> bool:
        if isinstance(distance, Distance):
            return self.meters == distance.meters
        if isinstance(distance, (float, int)):
            return self.meters == distance
        return False

    def __add__(self, distance: "Distance" or float | int) -> "Distance":
        if isinstance(distance, Distance):
            return Distance(self.meters + distance.meters)
        if isinstance(distance, (float, int)):
            return Distance(self.meters + distance)
        raise TypeError(
            f"distance must be utils_graph.Distance, float or int, not {type(distance)}")

    def __sub__(self, distance: "Distance" or float | int) -> "Distance":
        if isinstance(distance, Distance):
            return Distance(self.meters - distance.meters)
        if isinstance(distance, (float, int)):
            return Distance(self.meters - distance)
        raise TypeError(
            f"distance must be utils_graph.Distance, float or int, not {type(distance)}")

    def __iadd__(self, distance: "Distance" or float | int):
        if isinstance(distance, Distance):
            self.meters += distance.meters
        elif isinstance(distance, (float, int)):
            self.meters += distance
        else:
            raise TypeError(
                f"distance must be utils_graph.Distance, float or int, not {type(distance)}")

        return self

    def __isub__(self, distance: "Distance" or float | int):
        if isinstance(distance, Distance):
            self.meters -= distance.meters
        elif isinstance(distance, (float, int)):
            self.meters -= distance
        else:
            raise TypeError(
                f"distance must be utils_graph.Distance, float or int, not {type(distance)}")

        return self

    @property
    def kilometers(self) -> float:
        return self.meters/1000


class Speed:
    def __init__(self, kilometers_hour: float | int):
        self.kilometers_hour = kilometers_hour

    def __str__(self) -> str:
        return f"{self.kilometers_hour} km/h"

    def __repr__(self) -> str:
        return f"<soteriareitti.Speed kilometers_hour={self.kilometers_hour}>"

    @property
    def meters_second(self) -> float:
        return self.kilometers_hour / 3.6


class Time:
    def __init__(self, minutes: float | int):
        self.minutes = minutes

    def __str__(self) -> str:
        return f"{self.minutes} min"

    def __repr__(self) -> str:
        return f"<soteriareitti.Time minutes={self.minutes}>"

    @property
    def seconds(self) -> float:
        return self.minutes * 60

    @property
    def hours(self) -> float:
        return self.minutes / 60


class GeoUtils:
    earth_radius = Distance(6378137)  # Earth radius in meters

    @staticmethod
    def calculate_distance(location_source: Location, location_target: Location) -> Distance:
        """ Calculate distance between two locations """
        difference_longitude = location_target.longitude_rad - location_source.longitude_rad
        difference_latitude = location_target.latitude_rad - location_source.latitude_rad

        # Haversine formula
        # https://www.movable-type.co.uk/scripts/latlong.html

        # pylint: disable-next=invalid-name
        a = math.sin(difference_latitude / 2)**2 + math.cos(location_source.latitude_rad) * \
            math.cos(location_target.latitude_rad) * math.sin(difference_longitude / 2)**2

        # pylint: disable-next=invalid-name
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

        # pylint: disable-next=invalid-name
        d = GeoUtils.earth_radius.meters * c

        return Distance(d)

    @staticmethod
    def calculate_time(location_source: Location, location_target: Location,
                       maxspeed: Speed) -> Time:
        """ 
        Calculate how long it takes to travel between two locations
        """

        distance = GeoUtils.calculate_distance(location_source, location_target)
        return Time(distance.meters / maxspeed.meters_second / 60)
