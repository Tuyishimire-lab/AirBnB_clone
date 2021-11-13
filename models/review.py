#!/usr/bin/python3
"""
Review class
"""
from models.base_model import BaseModel

class Review(BaseModel):
	"""
	inherits from the base Model
	"""
	place_id = ""
	user_id = ""
	text = ""
	
