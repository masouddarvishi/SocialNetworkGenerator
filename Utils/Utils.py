import json


def decode_json(file_url):
    """ Receives a file url and return a Json object"""
    data = json.load(open(file_url, 'r'))
    print(data)