from typing import List


class Solution:
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        year_num = [0] * 100
        for i in range(len(birth)):
            for index in range(birth[i], death[i]):
                year_num[index - 1900] += 1
        max_year = 0
        max_unm = year_num[0]
        for y, n in enumerate(year_num):
            if max_unm < n:
                max_unm = n
                max_year = y
        return max_year + 1900
