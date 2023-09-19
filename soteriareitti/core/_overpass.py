""" soteriareitti/overpass_api.py """
import logging
import overpy

from soteriareitti.utils.settings import Settings
from soteriareitti.utils.overpass import OverpassUtils
from soteriareitti.utils.geo import Location, Distance


class OverpassAPI:

    def __init__(self):
        self._api = overpy.Overpass()

        self._maxsize = Settings.max_size
        self._timeout = Settings.timeout or 30

    def get_place_data(self, place: str) -> overpy.Result:
        """ Get overpass data from a place name """
        logging.debug("Starting overpass place query with: %s", place)

        query_str = OverpassUtils.generate_place_query(place, self._maxsize, self._timeout)
        logging.debug("Running query: %s", query_str)

        result = self._api.query(query_str)

        logging.debug("Overpass place query done")

        return result

    def get_around_data(self, center: Location, radius: Distance) -> overpy.Result:
        """ Get overpass data around a center location """
        logging.debug("Starting overpass around query with center: %s", center)

        query_str = OverpassUtils.generate_around_query(
            center, radius, self._maxsize, self._timeout)

        logging.debug("Running query: %s", query_str)

        result = self._api.query(query_str)

        logging.debug("Overpass around query done")

        return result
