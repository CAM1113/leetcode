from typing import List



class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        if len(s) <= 1:
            return s
        sets = [i for i in range(len(s))]
        for it in pairs:
            val1 = it[0]
            val2 = it[1]
            set_mask1 = sets[val1]
            set_mask2 = sets[val2]
            if set_mask1 == set_mask2:
                continue
            for i in range(len(sets)):
                if sets[i] == set_mask2:
                    sets[i] = set_mask1




def main():
    s = "dcab"
    pairs = [[0, 3], [1, 2], [0, 2]]
    print(Solution().smallestStringWithSwaps(s,pairs))

if __name__ == '__main__':
    main()