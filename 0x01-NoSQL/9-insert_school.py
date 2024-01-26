#!/usr/bin/env python3
"""module to list all in python
"""


def insert_school(mongo_collection, **kwargs):
    """function to do the module work
    """
    return mongo_collection.insert_one(kwargs).inserted_id


if __name__ == '__main__':
    """to prevent code execution when importing
    """
    pass
