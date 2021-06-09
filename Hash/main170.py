import collections


class TwoSum:

    def __init__(self):
        self.num_cnt_dic = collections.defaultdict(lambda: 0)

    def add(self, number: int) -> None:
        self.num_cnt_dic[number] += 1

    def find(self, value: int) -> bool:
        keys = self.num_cnt_dic.keys()
        if len(keys) < 1 or (len(keys) == 1 and self.num_cnt_dic.values()[0] < 2):
            return False
        for n in keys:
            if value - n == n:
                if self.num_cnt_dic[n] > 1:
                    return True
            elif value - n in keys:
                return True
        return False
