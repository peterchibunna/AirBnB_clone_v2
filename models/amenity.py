#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Represents an Amenity"""

    __tablename__ = "amenities"
    # if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    name = Column(String(128), nullable=False, default="")
    place_amenities = relationship(
        "Place", secondary="place_amenity", viewonly=False)
    # else:
    #     name = ""
