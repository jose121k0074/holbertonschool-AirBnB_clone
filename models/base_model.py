#!/usr/bin/python3
"""
A class that defines all common attributes/methods for other classes
"""


from datetime import datetime
import uuid


class BaseModel():
    """
    A class that defines all common attributes/methods for other classes
    """
    
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
    """
    A method that print a string representation
    """

    return "[{}] ({}) {}".format(self.__class__.__name__,
            self.id, self.__dict__)

    def save(self):
    """
    A method updates the public instance attrib updated_at with
    the current datetime
    """
    
    self.updated_at = datetime.utcnow()

    def to_dict(self):
    """
    A method returns a dict containing all keys/values of
    __dict__ of the instance
    """

    dict_new = {}
    for att in self.__dict__:
        if att in ["created_at", "updated_at"]:
            dict_new[att] = getattr(self, att).isoformat()
        else:
            dict_new[att] = getattr(self, att)
    dict_new['__class__'] = self.__class__.__name__
    return (dict_new)
