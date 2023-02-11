#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNB SHELL"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """End of File\n"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
