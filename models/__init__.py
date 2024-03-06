#!/usr/bin/python3
"""
Update this file. Creating a unique Filestorage instance
"""


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User

dict_class = {'BaseModel': BaseModel, 'User': User}

storage = FileStorage()
storage.reload()
