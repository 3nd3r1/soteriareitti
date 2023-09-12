""" soteriareitti/utils/utils_geo.py """
import math


class Location:
    """ Location class represents a point location on a map"""

    def __init__(self, longitude: float, latitude: float):
        """ 
        Initialize a location with longitude and latitude 

        Remember that longitude is the x-axis and latitude is the y-axis
        Longitude and latitude are in degrees
        """
        self.longitude = longitude
        self.latitude = latitude

    def __str__(self):
        return f"Location: ({self.longitude}, {self.latitude})"

    def as_tuple(self) -> tuple[float, float]:
        return (self.longitude, self.latitude)

    @property
    def longitude_rad(self) -> float:
        """ Return longitude in radians """
        return math.radians(self.longitude)

    @property
    def latitude_rad(self) -> float:
        """ Return latitude in radians """
        return math.radians(self.latitude)


class Distance:
    """ Distance class represents a distance on the map"""

    def __init__(self, distance_meters: float):
        self.__distance_meters = distance_meters

    @property
    def meters(self) -> float:
        return self.__distance_meters

    @property
    def kilometers(self) -> float:
        return self.__distance_meters/1000


class BoundingBox:
    """
    BoundingBox class represents a bounding box on the map

    min_location is the bottom left corner of the box 
    max_location is the top right corner of the box
    """

    def __init__(self, min_location: Location, max_location: Location):
        self.min_location = min_location
        self.max_location = max_location

    def __str__(self):
        return f"Bounding box from {self.min_location} to {self.max_location}"

    def as_tuple(self) -> tuple[float, float, float, float]:
        return self.min_location.as_tuple() + self.max_location.as_tuple()

    def as_polygon(self) -> list[tuple[float, float]]:
        top_left = Location(self.min_location.longitude, self.max_location.latitude).as_tuple()
        top_right = self.max_location.as_tuple()
        bottom_right = Location(self.max_location.longitude, self.min_location.latitude).as_tuple()
        bottom_left = self.min_location.as_tuple()

        return [top_left, top_right, bottom_right, bottom_left]


class GeoUtils:
    earth_radius = Distance(6378137)  # Earth radius in meters

    @staticmethod
    def calculate_bbox(location: Location, distance: Distance) -> BoundingBox:
        """ Calculate a bounding box from a location that is distance large"""
        latitude_rad = math.radians(location.latitude)

        angular_distance = distance.meters / GeoUtils.earth_radius.meters

        latitude_offset = angular_distance
        longitude_offset = angular_distance / math.cos(latitude_rad)

        latitude_offset_deg = math.degrees(latitude_offset)
        longitude_offset_deg = math.degrees(longitude_offset)

        min_latitude = location.latitude - latitude_offset_deg
        min_longitude = location.longitude - longitude_offset_deg
        max_latitude = location.latitude + latitude_offset_deg
        max_longitude = location.longitude + longitude_offset_deg

        min_location = Location(min_longitude, min_latitude)
        max_location = Location(max_longitude, max_latitude)

        return BoundingBox(min_location, max_location)

    @staticmethod
    def calculate_distance(location_source: Location, location_target: Location) -> Distance:
        """ Calculate distance between two locations """
        latitude_source_rad = math.radians(location_source.latitude)
        longitude_source_rad = math.radians(location_source.longitude)
        latitude_target_rad = math.radians(location_target.latitude)
        longitude_target_rad = math.radians(location_target.longitude)

        difference_longitude = longitude_target_rad - longitude_source_rad
        difference_latitude = latitude_target_rad - latitude_source_rad

        # Haversine formula
        # https://www.movable-type.co.uk/scripts/latlong.html

        # pylint: disable-next=invalid-name
        a = math.sin(difference_latitude / 2)**2 + math.cos(latitude_source_rad) * \
            math.cos(latitude_target_rad) * math.sin(difference_longitude / 2)**2

        # pylint: disable-next=invalid-name
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

        # pylint: disable-next=invalid-name
        d = GeoUtils.earth_radius.meters * c

        return Distance(d)
