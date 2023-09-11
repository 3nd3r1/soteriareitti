# soteriareitti/overpass_api.py

import overpy
from utils.settings import Settings
from utils.logger import logger


class OverpassAPI:
    overpass_settings = "[out:json][timeout:{timeout}]{maxsize}"
    overpass_search = "area[name='{name}']->.searchArea"
    overpass_filter = (
        f'["highway"]["area"!~"yes"]["access"!~"private"]'
        f'["highway"!~"abandoned|bridleway|bus_guideway|construction|corridor|cycleway|elevator|'
        f"escalator|footway|no|path|pedestrian|planned|platform|proposed|raceway|razed|steps|"
        f'track"]'
        f'["motor_vehicle"!~"no"]["motorcar"!~"no"]'
        f'["service"!~"emergency_access|parking|parking_aisle|private"]'
    )

    def __init__(self):
        self._api = overpy.Overpass()
        self._timeout = str(Settings.timeout)
        self._maxsize = ""

        if Settings.max_size:
            self._maxsize = f"[maxsize:{Settings.max_size}]"

    def get_overpass_data(self, place) -> overpy.Result:
        logger.debug("Starting overpass query")
        op_settings = OverpassAPI.overpass_settings.format(
            timeout=self._timeout, maxsize=self._maxsize)
        op_search = OverpassAPI.overpass_search.format(name=place)
        op_filter = OverpassAPI.overpass_filter

        query_str = f"{op_settings};{op_search};(way(area.searchArea){op_filter};>;);out;"

        result = self._api.query(query_str)
        logger.debug("Overpass query done")
        return result
