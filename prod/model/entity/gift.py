from prod.model.entity import *


class Gift:
    def __init__(self):
        self._sweets = []
        self._name = []

    def add(self, sweet):
        if isinstance(sweet, Sweet):
            self._sweets.append(sweet)
            self._name.append(sweet.name)

    def __bool__(self):
        return len(self._sweets) != 0

    def __len__(self):
        return len(self._sweets)

    def __getitem__(self, item):
        return self._sweets[item]

    def __setitem__(self, key, value):
        self._sweets[key] = value

    def __delitem__(self, key):
        del self._sweets[key]

    def __iter__(self):
        return iter(self._sweets)

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        self.__index += 1
        return self._sweets[self.__index]

    def get(self, index):
        if isinstance(index, int) and 0 <= index < self.size():
            return self._sweets[index]

    def size(self):
        return len(self._sweets)

    def __str__(self):
        return " ".join(self._name)

    def sort_by_name(self):
        self._name.sort()

