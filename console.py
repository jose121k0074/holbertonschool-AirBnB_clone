#!/usr/bin/python3
"""
A module cmd that contains the entry point of the command interpreter
"""


import cmd
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import shlex


class HBNBCommand(cmd.Cmd):
    """
    A class HBNH interpreter command
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        A command to exit of the program
        """
        return True

    def do_EOF(self, arg):
        """
        A command to exit of the program
        """
        print()
        return True

    def emptyline(self):
        """
        A method that when an empty line + ENTER shouldn’t execute anything
        """
        pass

    def do_create(self, arg):
        """ A command that creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if not arg:
            print("** class name missing **")
        elif arg not in "BaseModel":
            print("** class doesn't exist **")
        else:
            new_ins = BaseModel()
            new_ins.save()
            print(new_ins.id)

    def do_show(self, arg):
        """ A command that show the class name and id
        """

        l_arg = shlex.split(arg)
        if len(l_arg) == 0:
            print("** class name missing **")
        elif l_arg[0] not in "BaseModel":
            print("** class doesn't exist **")
        elif len(l_arg) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(l_arg[0], l_arg[1])
            temp = models.storage.all()
            if key in temp:
                print (temp[key])
            else:
                print ("** no instance found **") 

    def do_destroy(self, arg):
        """ A command that show the class name and id
        """
        l_arg = shlex.split(arg)
        if len(l_arg) == 0:
            print("** class name missing **")
        elif l_arg[0] not in "BaseModel":
            print("** class doesn't exist **")
        elif len(l_arg) == 1:
            print("** instance id missing **")
        else:
        	key = "{}.{}".format(l_arg[0], l_arg[1])
            temp = models.storage.all()
            if key in temp:
                del (temp[key])
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        A command prints all string representation of all instances based or
        not on the class name
        """
        l_arg = shlex.split(arg)
        list_obj = []
        temp = models.storage.all()

        if (arg and l_arg[0] in "BaseModel") or len(l_arg) == 0:
            for key, value in temp.items():
                list_obj.append(str(value))
            print(list_obj)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        A command that Updates an instance based on the class name and
        id by adding or updating attribute
        """
        l_arg = shlex.split(arg)
        if len(l_arg) == 0:
            print("** class name missing **")
        elif l_arg[0] not in "BaseModel":
            print("** class doesn't exist **")
        elif len(l_arg) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(l_arg[0], l_arg[1])
            temp = models.storage.all()
            if key not in temp:
                print("** no instance found **")
            elif len(l_arg) == 2:
                print("** attribute name missing **")
            elif len(l_arg) == 3:
                print("** value missing **")
            else:
                new_obj = temp.get(key)
                setattr(new_obj, l_arg[2], l_arg[3])
                models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
