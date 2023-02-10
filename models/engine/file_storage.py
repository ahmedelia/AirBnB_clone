#!/usr/bin/python3
"""
    the module thats serializes instances
    to a JSON file and deserializes JSON
    file to instances
"""
import json


class FileStorage():
    """FIle Storage Engine"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """add object to list of objects"""
        key = str(obj.__class__.__name__) + '.' + str(obj.__dict__["id"])
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """save all data to file"""
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """reload data from file"""
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                FileStorage.__objects = json.load(f)
        except Exception:
            return
