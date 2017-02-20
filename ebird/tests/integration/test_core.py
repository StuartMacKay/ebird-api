# -*- coding: utf-8 -*-

from unittest import TestCase

from ebird.core import \
    geo_observations, geo_species, geo_notable, \
    hotspot_observations, hotspot_species, hotspot_notable, \
    location_observations, location_species, location_notable, \
    region_observations, region_species, region_notable, \
    nearest_species, list_locations, find_locations, list_hotspots, \
    nearest_hotspots, list_species


class CoreIntegrationTests(TestCase):
    """Tests for the core functions which call the eBird API."""

    @classmethod
    def setUpClass(cls):
        records = region_notable('US-NY', detail='full', hotspot=True)
        cls.lat = "%.2f" % records[0]['lat']
        cls.lng = "%.2f" % records[0]['lng']
        cls.species = records[0]['sciName']
        cls.region = records[0]['subnational2Code']
        cls.location = records[0]['locID']

    def test_geo_observations(self):
        geo_observations(self.lat, self.lng)

    def test_geo_species(self):
        geo_species(self.species, self.lat, self.lng)

    def test_geo_notable(self):
        geo_notable(self.lat, self.lng)

    def test_hotspot_observations(self):
        hotspot_observations(self.location)

    def test_hotspot_species(self):
        hotspot_species(self.species, self.location)

    def test_hotspot_notable(self):
        hotspot_notable(self.location)

    def test_location_observations(self):
        location_observations(self.location)

    def test_location_species(self):
        location_species(self.species, self.location)

    def test_location_notable(self):
        location_notable(self.location)

    def test_region_observations(self):
        region_observations(self.region)

    def test_region_species(self):
        region_species(self.species, self.region)

    def test_region_notable(self):
        region_notable(self.region)

    def test_nearest_species(self):
        nearest_species(self.species, self.lat, self.lng)


# noinspection PyMethodMayBeStatic
class LocationsIntegrationTests(TestCase):
    """Tests for the locations functions which call the eBird API."""

    def test_list_locations(self):
        list_locations('country')

    def test_find_locations(self):
        find_locations('subnational1', match='west')

    def test_list_hotspots(self):
        list_hotspots('US-NV', back=10)

    def test_nearest_hotspots(self):
        nearest_hotspots(42.46, -71.25, back=1)

    def test_list_species(self):
        list_species()
