from yaml import load, FullLoader
from collections.abc import Mapping
import re


class Content(Mapping):
    __delimeter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)


    def load(self, cls, string):
        _, fm, content = self.__regex.split(string[2])

        load(fm, )

        return cls(metadata, content)


    def __init__(self, metadata, content):
        self.data = metadata
        self.data = {'content': content}


    @property


    def __iter__(self):
        return self.data

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        data = {}
        str(data)

