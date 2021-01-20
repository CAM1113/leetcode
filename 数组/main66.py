from typing import List


def add(digital: List[int], index):
    if abs(index) == len(digital):
        d = digital[index] + 1
        if d <= 9:
            digital[index] = d
        else:
            digital.insert(0, 1)
            digital[index] = d % 10
        return digital
    d = digital[index] + 1
    if d <= 9:
        digital[index] = d
    else:
        digital[index] = d % 10
        add(digital, index - 1)
    return digital


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
       return add(digits, -1)
