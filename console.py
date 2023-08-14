#!/usr/bin/python3
"""Defines the HBNBCommand class for the command interpreter."""

import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBnB project."""

    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def default(self, arg):
        """Handle invalid input."""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[: match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][: match.span()[0]], match.group(1)]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown command: {}".format(arg))
        return False

    def do_quit(self, line):
        """Exit the command interpreter."""
        return True

    def do_EOF(self, line):
        """Exit the command interpreter when EOF (Ctrl-D) is encountered."""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, line):
        """Create a new instance of a specified class."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_destroy(self, line):
        """Destroy a specified instance by id."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Show all instances of a specified class or all classes."""
        args = line.split()
        if not args:
            objects = storage.all()
        else:
            class_name = args[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            objects = {
                    k: v for k, v in storage.all().items()
                    if k.split('.')[0] == class_name
                    }

        instances = [str(obj) for obj in objects.values()]
        print(instances)

    def do_show(self, line):
        """Show the information about a specified instance by id."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_update(self, line):
        """Update attributes of a specified instance by id."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in storage.all():
            instance = storage.all()[key]
            if len(args) < 4:
                print("** attribute name missing **")
                return
            attr_name = args[2]
            attr_value = args[3]
            setattr(instance, attr_name, attr_value)
            instance.save()
        else:
            print("** no instance found **")

    def do_count(self, line):
        """Return the number of instances of a class."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        count = 0
        for key in storage.all():
            if key.startswith(class_name + "."):
                count += 1

        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
