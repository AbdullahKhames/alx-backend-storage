#!/usr/bin/env python3
"""module to list all in python
"""


def schools_by_topic(mongo_collection, topic):
    """function to do the module work
    """
    return mongo_collection.find( { "topics": topic } )


if __name__ == '__main__':
    """to prevent code execution when importing
    """
    pass
