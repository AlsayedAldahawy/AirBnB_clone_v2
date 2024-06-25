#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls == None or not cls:
            return FileStorage.__objects

        className = str(cls).split('.')[2].split("'")[0]
        return {k: v for k, v in FileStorage.__objects.items() if k.startswith(className)}

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes an instance based on the object passed.

        This method deletes an instance from the '__objects' dictionary of the 'FileStorage' class.
        It searches for the object in the values of the '__objects' dictionary. If found, it retrieves
        the corresponding key and deletes the key-value pair from the dictionary.

        Parameters:
        - obj (object): The object to be deleted from the storage.

        Returns:
        None
        """
        if obj in FileStorage.__objects.values():
            # Retrieve the key for the object to be deleted
            keyToDelete = next(
                k for k, v in FileStorage.__objects.items() if v == obj)
            # Delete the key-value pair from the dictionary
            del FileStorage.__objects[keyToDelete]
        else:
            pass
