#!/usr/bin/env python3
"""module to list all in python
"""
from pymongo import MongoClient


def fun():
    """
    function to list nginx logs
    """
    client = MongoClient("mongodb://localhost:27017/")
    nginx = client.logs.nginx
    print(f"{nginx.count_documents({})} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print(
            "\tmethod {}: {}".format(
                method, nginx.count_documents({"method": method}))
        )

    print(
        "{} status check".format(
            nginx.count_documents({"method": "GET", "path": "/status"}))
    )


if __name__ == '__main__':
    """to prevent code execution when importing
    """
    fun()
