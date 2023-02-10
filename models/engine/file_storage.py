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
        return __objects

    def new(self, obj):
        key = str(obj.__dict__["__class__"] + obj.__dict__["id"])
        __objects[key] = obj

    def save(self):
        with open(__file_path, 'w', encoding="utf-8") as f:
            return json.dump(__objects, f)

    def reload(self):
        try:
            with open(__file_path, 'r', encoding="utf-8") as f:
                __objects = json.load(f)
        except Exception:
            return
