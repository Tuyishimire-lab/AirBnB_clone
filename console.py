#!/usr/bin/python3
"""
Entry to command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
	"""
	entry to command interpreter
	"""
	prompt = "(hbnb)"
	classes = {"BAseModel", "State", "City", "Amenity", "Place", "Review", "User"}

	def do_EOF(self, line):
		"""
		Exit on Ctrl-D
		"""
		print()
		return True
	def do_quit(self, line):
		"""
		exit on quit
		"""
		return True
	def emptyline(self):
		"""
		respondible for overwrittingdefault beahavior
		"""
		pass
	def do_create(self, line):
		"""
		create instances specified by the user
		"""
		if len(line) == 0:
			print("** class name missing**")
		elif line not in HBNBCommand.classes:
			print("** class doesn't exist**")
		else:
			instance = eval(line)()
			instance.save()
			print(instance.id)
	def do_show(self, line):
		"""
		prints string representation by name and Id
		"""
		if len(line) == 0:
			print("** class name missing **")
			return
		args = parse(line)
		if args[0] not in HBNBCommand.classes:
			print("**class doesn't exist**")
			return
		try:
			if args[1]:
				name = "{}.{}".format(args[0], args[1])
				if name not in storage.all().keys():
					print("** no instance found**")
				else:
					print(storage.all()[name])
		except IndexError:
			print("**Instance id missing**")
	def do_destroy(self, line):
		"""
		Destroy instnce  created by the user
		and save changes to the json file
		"""
		if len(line) == 0:
			print("** class name missing**")
			return
		args = parse(line)
		if args[0] not in HBNBCommand.classes:
			print("**class doesn't exist**")
			return
		try:
			if args[1]:
				name = "{}.{}".format(args[0], args[1])
				if name not in storage.all().keys():
					print("** no instance found**")
				else:
					del storage.all()[name]
					storage.save()
		except IndexError:
			print("** instance id missing **")
	def do_all(self, line):
		"""
		prints all objects or all objects 
		of a specific class
		"""
		args = parse(line)
		obj_list = []
		if len(line) == 0:
			for objs in storage.all().values():
				obj_list.append(objs)
			print(obj_list)
		elif args[0] in HBNBCommand.classes:
			for key, objs in storage.all().items():
				if args[0] in key:
					obj_list.append(objs)
			print(obj_list)
		else:
			print("** class doesn't exist**")
	def do_update(self, line):
		"""
		it will do update if given  right  input
		"""
		args = parse(line)
		if len(args) >= 4:
			key = "{}.{}".format(args[0], args[1])
			cast = type(eval(args[3]))
			arg3 = args[3]
			arg3 = arg3.strip('"')
			arg3 = arg3.strip("'")
			setattr(storage.all()[key], args[2], cast(arg3))
			storage.all()[key].save()
		elif len(args) == 0:
			print("** class name missing**")
		elif args[0] not in HBNBCommand.classes:
			print("**class doesn't exist**")
		elif len(args) == 1:
			print("**instance id missing**")
		elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
			print("** no instance found**")
		elif len(args) == 2:
			print("** attribute name missing **")
		else:
			print("** valuse missing** ")
	def do_count(self, line):
		"""
		counts of iintsnces displayed
		"""
		if line in HBNBcommand.classes:
			count = 0
			for key, objs in storage.all().items():
				if line in key:
					count += 1
			print(count)
		else:
			print("**class doesn't exist**")
	def default(self, line):
		"""
		accepts class and its arguments
		"""
		args = line.split('.')
		class_arg = args[0]
		if len(args) == 1:
			print("** UNknown syntax: {}".format(line))
			return
		try:
			args = args[1].split('(')
			command = args[0]
			if command == 'all':
				HBNBCommand.do_all(self, class_arg)
			elif command == 'count':
				HBNBCommand.do_count(self, class_arg)
			elif command == 'show':
				args = args[1].split(')')
				id_arg = args[0]
				id_arg = id_arg.strip("'")
				id_arg = id_arg.strip('"')
				arg = class_arg + ' ' + id_arg
				HBNBCommand.do_show(self, arg)
			elif command == 'destroy':
				args = args[1].split(')')
				id_arg = args[0]
				id_arg = id_arg.strip('"')
				id_arg = id_arg.strip("'")
				arg = class_arg + ' ' + id_arg
				HBNBCommand.do_destroy(self, arg)
			elif command == 'update':
				args = args[1].split(',')
				id_arg = args[0].strip("'")
				id_arg = id_arg.strip('"')
				name_arg = args[1].strip(',')
				val_arg = args[2]
				name_arg = name_arg.strip(' ')
				name_arg = name_arg.strip("'")
				name_arg = name_arg.strip('"')
				val_arg = val_arg.strip(' ')
				val_arg = val_arg.strip(')')
				arg = class_arg + ' ' + id_arg + ' ' + name_arg + ' ' + val_arg
				HBNBCommand.do_update(self, arg)
			else:
				print("** UNknown syantax: {}".format(line))
		except IndexError:
			print("** Unknown syntax: {}".format(line))
	def parse(line):
		"""
		Helper for user to ype input
		"""
		return tuple(line.split())

	if __name__ == "__main__":
		HBNBCommand().cmdloop()
