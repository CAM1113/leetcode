from typing import List


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        level = set()
        level.add((0, False))
        jump_times = 0
        past_p = set()
        max_p = 6000
        if 0 == x:
            return jump_times
        while len(level) > 0:
            jump_times += 1
            next_level = set()
            for p in level:
                past_p.add(p[0])
                if not p[1] and p[0] - b > 0 and (p[0] - b) not in forbidden and (p[0] - b) not in past_p:
                    if p[0] - b == x:
                        return jump_times
                    next_level.add((p[0] - b, True))

                if p[0] + a not in forbidden and p[0] + a not in past_p:
                    if p[0] + a == x:
                        return jump_times
                    if p[0] + a < max_p:
                        next_level.add((p[0] + a, False))
            level = next_level
        return -1


if __name__ == '__main__':
    f = [1998]
    aa = 1999
    bb = 2000
    xx = 2000
    print(Solution().minimumJumps(f, aa, bb, xx))
