""" soteriareitti/utils/utils_overpass.py """
from utils.utils_geo import Location, Distance


class OverpassUtils:
    op_settings = "[out:json][timeout:{timeout}]{maxsize}"
    op_search = "area[name='{name}']->.searchArea"
    op_filter = (
        f'["highway"]["area"!~"yes"]["access"!~"private"]'
        f'["highway"!~"abandoned|bridleway|bus_guideway|construction|corridor|cycleway|elevator|'
        f"escalator|footway|no|path|pedestrian|planned|platform|proposed|raceway|razed|steps|"
        f'track"]'
        f'["motor_vehicle"!~"no"]["motorcar"!~"no"]'
        f'["service"!~"emergency_access|parking|parking_aisle|private"]'
    )

    @staticmethod
    def generate_place_query(place: str, maxsize: int | None = None, timeout: int = 30) -> str:
        """ Generate an overpass query that searches for nodes and ways in a place """

        op_maxsize = f"[maxsize:{maxsize}]" if maxsize else ""
        op_timeout = str(timeout) if timeout else "30"

        op_settings = OverpassUtils.op_settings.format(maxsize=op_maxsize, timeout=op_timeout)
        op_search = OverpassUtils.op_search.format(name=place)
        op_filter = OverpassUtils.op_filter

        return f"{op_settings};{op_search};(way(area.searchArea){op_filter};>;);out;"

    @staticmethod
    def generate_location_query(location: Location, radius: Distance,
                                maxsize: int | None = None, timeout: int = 30) -> str:
        """ Generate an overpass query that searches for nodes around a location """

        op_maxsize = f"[maxsize:{maxsize}]" if maxsize else ""
        op_timeout = str(timeout) if timeout else "30"

        op_settings = OverpassUtils.op_settings.format(maxsize=op_maxsize, timeout=op_timeout)
        op_filter = OverpassUtils.op_filter

        return f"{op_settings};(node(around:{radius.meters},{location.latitude},\
            {location.longitude}){op_filter};);out;"
