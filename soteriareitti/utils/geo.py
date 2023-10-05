""" soteriareitti/utils/geo.py """
import math
from soteriareitti.classes.geo import Location, Distance, Speed, Time


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
