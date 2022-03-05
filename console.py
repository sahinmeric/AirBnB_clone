#!/usr/bin/python3
"""
This script containts the entry point of
the command interpreter
"""


import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ Command line interpreter"""
    prompt = "(hbtn) "
    class_list = ['BaseModel', 'User', 'State', 'City',
                  'Amenity', 'Place', 'Review']

    def do_EOF(self, arg):
        """EOF Quits from the program"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """ empty line handle"""
        pass

    def do_create(self, arg):
        """ creates an instance of given class"""
        if arg:
            if arg in self.class_list:
                print("Exists")  # TODO
            else:
                print("class doesn't exist")
        else:
            print("class name missing")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
