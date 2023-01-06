#!/usr/bin/python3
""" unittest cases for the Amenity model"""
from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity


class TestAmenity(TestBaseModel):
    """unittest cases for the Amenity model """

    def __init__(self, *args, **kwargs):
        """ initialize an Amenity """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name(self):
        """Test the name of an Amenity instance"""
        new = self.value()
        self.assertEqual(type(new.name), str)
