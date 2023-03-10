#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

import ast
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand"""
    prompt = "(hbnb) "
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """End of File"""
        print("")
        return True

    def do_create(self, line):
        """Creates a new instance of a CLass """
        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            tmp = HBNBCommand.classes[line]()
            tmp.save()
            print("{}".format(tmp.id))

    def do_show(self, line):
        """ Prints the string representation of an instance """

        tmp = line
        line = line.split(" ")
        if line[0] == "":
            print("** class name missing **")
        elif len(line) == 1 and line[0] in HBNBCommand.classes:
            print("** instance id missing **")
        elif line[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            key = line[0] + "." + line[1]
            objects = storage.all()
            if key in objects:
                obj = HBNBCommand.classes[line[0]](**objects[key])
                print(obj)
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id"""
        tmp = line
        line = line.split(" ")
        if line[0] == "":
            print("** class name missing **")
        elif len(line) == 1 and line[0] in HBNBCommand.classes:
            print("** instance id missing **")
        elif line[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            key = line[0] + "." + line[1]
            objects = storage.all()
            if key in objects:
                storage.delete(key)
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances"""

        if line and line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            list = []
            objects = storage.all()
            for key, value in objects.items():
                clss = key.split('.')[0]
                if line and clss == line:
                    list.append(str(HBNBCommand.classes[line](** value)))
                elif not line:
                    list.append(str(HBNBCommand.classes[clss](** value)))
                else:
                    continue
            print(list)

    def do_update(self, line):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        """
        line = line.split(" ")
        objects = storage.all()
        if line[0] == "":
            print("** class name missing **")
        elif line[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        elif str(line[0]+'.'+line[1]) not in objects:
            print("** no instance found **")
        elif len(line) == 2:
            print("** attribute name missing **")
        elif len(line) == 3:
            print("** value missing **")
        else:
            key = str(line[0]+'.'+line[1])
            dic = objects[key]
            obj = HBNBCommand.classes[line[0]](**dic)
            storage.delete(key)
            try:
                line[3] = ast.literal_eval(line[3])
            except Exception:
                pass
            setattr(obj, line[2], line[3])
            storage.new(obj)
            storage.save()

    def emptyline(self):
        """EmptyLIne"""
        pass

    def default(self, line):
        """Default method """
        line = line.split('.')
        if len(line) == 1:
            print("*** Unknown syntax: {}".format(line))
            return
        clss = line[0]
        line = line[1].split('(')
        command = line[0]
        if clss not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if command == 'all':
            self.do_all(clss)

        elif command == 'show':
            if line[-1][:-1] == "":
                print("** instance id missing **")
            else:
                self.do_show(clss + " " + str(line[-1][:-1]))

        elif command == 'count':
            cnt = 0
            objects = storage.all()
            for key in objects.keys():
                k = key.split('.')[0]
                if k == clss:
                    cnt = cnt + 1
            print(cnt)
        elif command == "destroy":
            if line[-1][:-1] == "":
                print("** instance id missing **")
            else:
                self.do_destroy(clss + " " + str(line[-1][:-1]))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
