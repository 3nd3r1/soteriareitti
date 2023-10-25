""" tests/test_geo.py """

import unittest
from soteriareitti.classes.geo import Location, Distance, Speed, Time
from soteriareitti.utils.geo import GeoUtils


class TestGeo(unittest.TestCase):
    """ Tests for the geo classes and GeoUtils methods """

    def test_geo_distance(self):
        """ Test that the Distance class works correctly """
        # Test that conversion from meters to kilometers works correctly
        distance = Distance(1000)

        self.assertEqual(distance.meters, 1000)
        self.assertEqual(distance.kilometers, 1)

        # Test that iadd works correctly
        distance += 1000
        self.assertEqual(distance.meters, 2000)
        self.assertEqual(distance.kilometers, 2)

        # Test that isub works correctly
        distance -= 1000
        self.assertEqual(distance.meters, 1000)
        self.assertEqual(distance.kilometers, 1)

        # Test that add and eq works correctly
        self.assertEqual(distance + 1000, 2000)

        # Test that sub and eq works correctly
        self.assertEqual(distance - 1000, 0)

    def test_geo_location(self):
        """ Test that the Location class works correctly """
        location = Location(60.0, 24.0)
        self.assertEqual(location.longitude, 24.0)
        self.assertEqual(location.latitude, 60.0)

        # Test invalid arguments
        self.assertRaises(TypeError, Location, "60.0", 24.0)

        # Test from_str
        location_from_str = Location.from_str("60.0,24.0")
        self.assertEqual(location_from_str.latitude, 60.0)
        self.assertEqual(location_from_str.longitude, 24.0)

        # Test __eq__
        self.assertEqual(location, Location(60.0, 24.0))
        self.assertEqual(location, (60.0, 24.0))

        # Test that radian conversion works correctly
        self.assertAlmostEqual(location.longitude_rad, 0.41887902047863906)
        self.assertAlmostEqual(location.latitude_rad, 1.0471975511965976)

        # Test as tuple
        self.assertEqual(location.as_tuple(), (60.0, 24.0))

        # Test rounding
        location = Location(60.123456789, 24.123456789)
        self.assertEqual(location.rounded(4), Location(60.1235, 24.1235))

    def test_geo_speed(self):
        """ Test that the Speed class works correctly """
        speed = Speed(36)
        self.assertEqual(speed.kilometers_hour, 36)
        self.assertEqual(speed.meters_second, 10)

    def test_geo_time(self):
        """ Test that the Time class works correctly """
        time = Time(60)
        self.assertEqual(time.seconds, 3600)
        self.assertEqual(time.minutes, 60)
        self.assertEqual(time.hours, 1)

    def test_geo_calculate_distance(self):
        """ Test that the calculate_distance function calculates the distance correctly """
        location_helsinki = Location(60.1699, 24.9384)
        location_vantaa = Location(60.2934, 25.0378,)
        distance = GeoUtils.calculate_distance(location_helsinki, location_vantaa)

        self.assertAlmostEqual(distance.kilometers, 14.8, delta=1)

    def test_geo_calculate_time(self):
        """ Test that the calculate_time function calculate the time correctly """
        location_helsinki = Location(60.1699, 24.9384)
        location_vantaa = Location(60.2934, 25.0378,)
        time = GeoUtils.calculate_time(location_helsinki, location_vantaa, Speed(100))

        self.assertAlmostEqual(time.minutes, 9, delta=0.5)
