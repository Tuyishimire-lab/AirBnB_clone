#!/user/bin/python3
from datetime import datetime
import uuid
import models

"""
The basemodel is the parent
of all classes

"""
class BaseModel():
	"""
	base class of the project
	methos used:
	__init__(self)
	__str__(self)
	__save(self)
	__repr__(self)
	to_dict(self)

	"""
	def __init__(self, *args, **kwargs):
		"""
		Attributes initialization
		"""
		if kwargs:
			for key, val in kwargs.items():
				if "creted_at" == key:
					self.created_at = datetime.strptime(kwargs["creted_at"],"%y-%m%dT%H:%M:%S.%f")
				elif "updated_at" == key:
					self.updated_at = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
				elif "__class__" == key:
					pass
				else:
					setattr(self, key, val)
		else:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.now()
			self.updated_at = datetime.now()
			models.storage.new(self)
	def __str__(self):
		"""
		info about model
		"""
		return('[{}]({}){}'.format(self.__class__.__name__,self.id, self.__dict__))
	def __repr__(self):
		"""
		String presentation
		"""
		return(self.__str__())
	def save(self):
		"""
		saving and updating serialized file
		"""
		self,updated_at = datetime.now()
		models.storage.save()
	def to_dict(self):
		"""
		adds class info to dic which its returns in
		a string format
		"""
		dic = {}
		dic["__class__"]= self.__class.__name__
		for k, v in self.__dict__.items():
			if isinstance(v, (datetime, )):
				dic[k] = v.isformat()
			else:
				dic[k] = v
		return dic

