#!/usr/bin/env python3
"""module to list all in python
"""


def top_students(mongo_collection):
    """
    returns all students sorted by average score
    """
    return mongo_collection.aggregate([
        {'$project': {
            'name': 1,
            'averageScore': {'$avg': '$topics.score'}
        }},
        {'$sort': {'averageScore': -1}}
    ])


if __name__ == '__main__':
    """to prevent code execution when importing
    """
    pass
