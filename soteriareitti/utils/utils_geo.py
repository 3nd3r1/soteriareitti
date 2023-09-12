""" soteriareitti/utils/utils_geo.py """
import math


class GeoUtils:
    @staticmethod
    def calculate_offset(location: tuple[float, float], distance: float):
        """ Calculate a bounding box offset from a location. Distance in meters """

        earth_radius = 6378137  # Earth radius in meters

        longitude_rad = math.radians(location[0])
        latitude_rad = math.radians(location[1])

        angular_distance = distance / earth_radius

        latitude_offset = angular_distance
        longitude_offset = angular_distance / math.cos(latitude_rad)

        latitude_offset_deg = math.degrees(latitude_offset)
        longitude_offset_deg = math.degrees(longitude_offset)

        min_latitude = location[1] - latitude_offset_deg
        min_longitude = location[0] - longitude_offset_deg
        max_latitude = location[1] + latitude_offset_deg
        max_longitude = location[0] + longitude_offset_deg

        return (min_longitude, min_latitude, max_longitude, max_latitude)
