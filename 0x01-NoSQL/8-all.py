#!/usr/bin/env python3
"""module to list all in python
"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """function to do the module work
    """
    data = []
    for s in mongo_collection.find():
        data.append(s)
    return data


if __name__ == '__main__':
    """to prevent code execution when importing
    """
    pass
