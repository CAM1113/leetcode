import collections
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt_dict = collections.defaultdict(int)
        for a in answers:
            cnt_dict[a] += 1
        sums = 0
        for k in cnt_dict:
            nums = cnt_dict[k]
            while nums > k + 1:
                sums += k + 1
                nums -= k + 1
            sums += k + 1
        return sums


if __name__ == '__main__':
    answers = []
    print(Solution().numRabbits(answers))
