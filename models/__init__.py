#!/usr/bin/python3
"""
Update this file. Creating a unique Filestorage instance
"""


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

dict_class = {'BaseModel': BaseModel,
              'User': User,
              'Place': Place,
              'State': State,
              'City': City,
              'Amenity': Amenity,
              'Review': Review}

storage = FileStorage()
storage.reload()
