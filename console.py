#!/usr/bin/python3
# console.py
# Alex Nuñez <5694@holbertonstudents.com>
# Yeff Espinoza <5153@holbertonstudents.com>
"""Define a console implementation."""


import cmd


class HBNBCommand(cmd.Cmd):
    """Represent a console of HBNBCommand."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program."""
        return (True)

    def do_EOF(self, arg):
        """Secures a clean exit."""
        return (True)

    def emptyline(self):
        """Stop the last executed command"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
