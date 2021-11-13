#!/usr/bin/python3
"""
File storage
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class FileStorage:
	"""
	Diserrializing and serializing json files
	"""
	__file_path = 'file.json'
	__objects = {}
	class_dict = {"BAseModel": BaseModel, "User": User, "State": State, "City": City,"Place": Place, "Review": Review, "Amenity": Amenity}
	def all(self):
		"""
		Returns Dictionary of class.i object's instance
		"""
		return self.__objects
	def new(self):
		"""
		Adds new object to the existing one in the dictionary
		"""
		if obj:
			key = '{}.{}'.format(obj.__class__.__name__, obj.id)
			self.__objects[key] = obj
	def save(self):
		"""
		saves object dictionary to json file
		"""
		my_dict = {}
		for key, obj in self.__objects.items():
			my_dict[key] = obj.to_dict()
		with open(self.__file_path, 'w') as f:
			json.dump(my_dict, f)
	def reload(self):
		"""
		if json file exissts, conver obj dictionary back to an instance
		"""
		try:
			with open(self.__file_path, 'r') as f:
				new_obj = jason.load(f)
			for key, val in new_obj.items():
				obj = self.class_dict[val['__class__']](**val)
				self.__objects[key] = obj
		except FileNotFoundError:
			pass
