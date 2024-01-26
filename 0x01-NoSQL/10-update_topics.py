#!/usr/bin/env python3
"""module to list all in python
"""


def update_topics(mongo_collection, name, topics):
    """function to do the module work
    """
    mongo_collection.update_many({ "name": name}, {"$set": {"topics": topics}})


if __name__ == '__main__':
    """to prevent code execution when importing
    """
    pass
