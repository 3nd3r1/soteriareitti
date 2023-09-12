""" soteriareitti/overpass_api.py """
import logging
import overpy

from utils.settings import Settings
from utils.utils_overpass import OverpassUtils
from utils.utils_geo import Location, Distance


class OverpassAPI:

    def __init__(self):
        self._api = overpy.Overpass()

        self._maxsize = Settings.max_size
        self._timeout = Settings.timeout or 30

    def get_place_data(self, place: str) -> overpy.Result:
        """ Get overpass data from a place name """
        logging.debug("Starting overpass place query with: %s", place)

        query_str = OverpassUtils.generate_place_query(place, self._maxsize, self._timeout)
        result = self._api.query(query_str)

        logging.debug("Overpass place query done")

        return result

    def get_location_nodes(self, location: Location, radius: Distance) -> overpy.Result:
        """ Get overpass data from a bounding_box of form (lon1, lat1, lon2, lat2)"""
        logging.debug("Starting overpass location area query with: %s", location)

        query_str = OverpassUtils.generate_location_query(
            location, radius, self._maxsize, self._timeout)
        result = self._api.query(query_str)

        logging.debug("Overpass location query done")

        return result
