import json


class JsonData:
    """ Class that holds the stats read in the file"""

    def __init__(self, file_url):
        file = open(file_url, 'r')
        data = json.load(file)
        self.__dict__ = data
