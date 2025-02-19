#!/usr/bin/python3
"""
defines a fonction that retuns
the JSON representation of an object
"""
import json
"""
import json to be use later
"""


def to_json_string(my_obj):
    """Returns representation of an object"""
    return json.dumps(my_obj)
