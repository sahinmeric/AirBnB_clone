#!/usr/bin/python3
"""
This script containts the entry point of
the command interpreter
"""


import cmd
import sys
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Command line interpreter"""
    prompt = "(hbnb) "
    class_list = ['BaseModel', 'User', 'State', 'City',
                  'Amenity', 'Place', 'Review']

    def do_EOF(self, arg):
        """EOF Quits from the program
        """
        return True

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """ empty line handle
        """
        pass

    def do_create(self, arg):
        """ creates an instance of given class
        """
        if arg:
            if arg in self.class_list:
                new_instance = eval(arg + "()")
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Prints the string representation of
        an instance based on the class name and id
        """
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg[0] not in self.class_list:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        else:
            if len(arg) > 1:
                key = arg[0] + "." + arg[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        else:
            if args[0] in self.class_list:
                if len(args) < 2:
                    print("** instance id missing **")
                elif (args[0] + "." + args[1]) in models.storage.all():
                    del models.storage.all()[(args[0] + "." + args[1])]
                    models.storage.save()
                else:
                    print("** class doesn't exist **")

    def do_all(self, arg):
        """ Prints all string representation of all instances
        based or not on the class name.
        """
        all_inst = models.storage.all()
        if arg:
            if arg in self.class_list:
                for obj in all_inst.values():
                    if type(obj).__name__ == arg:
                        print(obj)
            else:
                print("** class doesn't exist **")
        else:
            for obj in all_inst.values():
                print(obj)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file)
        """
        all_inst = models.storage.all()
        arg = arg.split('"')
        if len(arg) > 1:
            new_value = arg[1]
        else:
            new_value = ""
        arg = arg[0].split()
        if len(arg):
            if arg[0] in self.class_list:
                if len(arg) > 2:
                    if (arg[0] + "." + arg[1]) in all_inst:
                        if len(arg) >= 3:
                            if new_value:
                                obj = all_inst[arg[0] + "." + arg[1]]
                                print(obj)
                                setattr(obj, arg[2], new_value)
                                obj.save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
