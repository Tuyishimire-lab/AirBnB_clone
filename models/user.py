#!/usr/bin/python3
"""
User Class
"""
from models.base_model import BaseModel
import json

class User(BaseModel):
	email = ""
	password = ""
	first_name = ""
	last_name = ""
