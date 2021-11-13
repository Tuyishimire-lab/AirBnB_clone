#!/usr/bin/python3
"""
Place class
"""
from models.base_model import BaseModel

class Place(BaseModel):
	"""
	INherits from the base model
	"""
	city_id = ""
	user_id = ""
	name = ""
	description = ""
	number_rooms = 0
	number_bathrooms = 0
	max_guest = 0
	price_by_night = 0.0
	latitude = 0.0
	amenity_ids = []

