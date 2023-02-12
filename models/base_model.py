#!/usr/bin/python3
"""
    the module thats contain
    base class of all classes
    in airbnb project
"""
# import sys
# sys.path.append(
#    "/home/yuu/AirBnB_clone/")
import uuid
import datetime
from models import storage


class BaseModel:
    """Base Model Class to be base for all classes"""

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            if key == "__class__":
                continue
            if key == "created_at":
                value = fromisoformat(value)
            if key == "updated_at":
                value = fromisoformat(value)
            setattr(self, key, value)

        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    @classmethod
    def fromisoformat(obj):
        """from iso format to datetime obj using in dict"""
        dt, _, us = obj.partition(".")
        dt = datetime.datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S")
        us = int(us.rstrip("Z"), 10)
        return dt + datetime.timedelta(microseconds=us)

    def __str__(self):
        """override str method  __str__ when print object or cast to str"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """save object save(self) and save in files"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """convert object to dict and return dictonary"""
        tmp_dict = self.__dict__.copy()
        tmp_dict["__class__"] = self.__class__.__name__
        tmp_dict["updated_at"] = self.updated_at.isoformat()
        tmp_dict["created_at"] = self.created_at.isoformat()
        return tmp_dict
