import collections
from random import Random


class RandomizedCollection:

    def __init__(self):
        self.data_dict = collections.OrderedDict()
        self.element_size = 0

    def insert(self, val: int) -> bool:
        is_contain = False
        try:
            num = self.data_dict[val]
            self.data_dict[val] = num + 1
        except KeyError as e:
            self.data_dict[val] = 1
            is_contain = True
        self.element_size = self.element_size + 1
        return is_contain

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        is_contain = True
        try:
            num = self.data_dict[val]
            self.element_size = self.element_size - 1
            if num == 1:
                del self.data_dict[val]
            else:
                self.data_dict[val] = num - 1
        except KeyError as e:
            is_contain = False
        return is_contain

    def getRandom(self) -> int:
        if self.element_size == 0:
            return
        index = Random().randint(a=0, b=self.element_size-1)
        for key in self.data_dict.keys():
            num = self.data_dict[key]
            if index <= num:
                return key
            else:
                index -= num


val = 5
obj = RandomizedCollection()
param_1 = obj.insert(val)
param_2 = obj.remove(val)
param_3 = obj.getRandom()
