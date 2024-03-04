#!/usr/bin/python3
"""
A module cmd that contains the entry point of the command interpreter
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """
    A class HBNH interpreter command
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        A method to exit of the program
        """
        return True

    def do_EOF(self, arg):
        """
        A method to exit of the program
        """
        print()
        return True

    def emptyline(self):
        """
        A method that when an empty line + ENTER shouldn’t execute anything
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
