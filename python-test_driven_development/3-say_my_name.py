#!/usr/bin/python3
"""write a function that prints My Name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """prints My Name is
        arguments
            first_name: a persons first name
            last_name: a persons last name
        return: My Name is <first_name> <last_name>
        """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
