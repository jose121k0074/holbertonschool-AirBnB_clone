#!/usr/bin/python3
"""
A class that defines all common attributes/methods for other classes
"""


from datetime import datetime
import uuid
import models


class BaseModel():
    """
    A class that defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        A method constructor of BaseModel. Define attributtes of Class parent
        """

        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)
            # self.__objects
        else:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key not in ['__class__']:
                    setattr(self, key, value)

    def __str__(self):
        """A method that print a string representation """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                    self.id, self.__dict__)

    def save(self):
        """
        A method updates the public instance attrib updated_at with
        the current datetime
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        A method returns a dict containing all keys/values of
        __dict__ of the instance
        """

        dict_new = self.__dict__.copy()
        dict_new["created_at"] = dict_new['created_at'].isoformat()
        dict_new["updated_at"] = dict_new['updated_at'].isoformat()
        dict_new['__class__'] = self.__class__ .__name__
        return (dict_new)
