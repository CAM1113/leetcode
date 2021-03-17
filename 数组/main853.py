from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        index = 1
        info = [[i, j] for i, j in zip(position, speed)]
        info.sort(key=lambda x: x[0],reverse=True)
        while index < len(info):
            t1 = (target - info[index - 1][0]) / info[index - 1][1]
            t2 = (target - info[index][0]) / info[index][1]
            if t1 >= t2:
                info.pop(index)
            else:
                index += 1
        return len(info)


if __name__ == '__main__':
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    print(Solution().carFleet(target, position, speed))
