from typing import List


def get_hash(s):
    ha = 0
    for index, c in enumerate(s):
        ha += (ord(c) - ord("0")) * (10 ** index)
    return ha


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        level = [["0", "0", "0", "0"]]
        used = set()
        step = -1
        d = [get_hash(c) for c in deadends]
        target = get_hash(target)
        while len(level) != 0:
            next_level = []
            step += 1
            for state in level:
                if get_hash(state) in used:
                    continue
                if get_hash(state) == target:
                    return step
                used.add(get_hash(state))
                for index in range(4):
                    if ord(state[index]) - 1 == ord("0") - 1:
                        char = "9"
                    else:
                        char = chr(ord(state[index]) - 1)
                    temp = state[:]
                    temp[index] = char
                    temp_hash = get_hash(temp)
                    if temp_hash not in used and temp_hash not in d:
                        next_level.append(temp)

                    if ord(state[index]) + 1 == ord("9") + 1:
                        char = "0"
                    else:
                        char = chr(ord(state[index]) + 1)
                    temp = state[:]
                    temp[index] = char
                    temp_hash = get_hash(temp)
                    if temp_hash not in used and temp_hash not in d:
                        next_level.append(temp)
            level = next_level
        return -1


if __name__ == '__main__':
    x = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
    t = "8888"
    print(Solution().openLock(x, t))
