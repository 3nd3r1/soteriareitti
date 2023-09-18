""" tests/test_utils_geo.py """

import unittest
from soteriareitti.utils.utils_geo import GeoUtils, Location, Distance


class TestUtilsGeo(unittest.TestCase):
    """ Tests for the utils_geo module """

    def test_geo_distance(self):
        """ Test that the Distance class works correctly """
        # Test that conversion from meters to kilometers works correctly
        distance = Distance(1000)

        self.assertEqual(distance.meters, 1000)
        self.assertEqual(distance.kilometers, 1)

        # Test that the _iadd_ method works correctly
        distance += 1000

        self.assertEqual(distance.meters, 2000)
        self.assertEqual(distance.kilometers, 2)

        # Test type safety

        self.assertRaises(TypeError, distance.__add__, "1000")
        self.assertEqual(distance.meters, 2000)

    def test_geo_location(self):
        """ Test that the Location class works correctly """
        location = Location(24.0, 60.0)
        self.assertEqual(location.longitude, 24.0)
        self.assertEqual(location.latitude, 60.0)

        # Test that radian conversion works correctly
        self.assertAlmostEqual(location.longitude_rad, 0.41887902047863906)
        self.assertAlmostEqual(location.latitude_rad, 1.0471975511965976)

        # Test as tuple
        self.assertEqual(location.as_tuple(), (24.0, 60.0))

    def test_geo_calculate_distance(self):
        """ Test that the calculate_distance function calculates the distance correctly """
        location_helsinki = Location(24.9384, 60.1699)
        location_vantaa = Location(25.0378, 60.2934)
        distance = GeoUtils.calculate_distance(location_helsinki, location_vantaa)

        self.assertAlmostEqual(distance.kilometers, 14.8, delta=1)
