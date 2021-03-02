from typing import List


class Solutio n:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        level = set()
        level.add((0, False))
        jump_times = 0
        past_p = set()
        max_p = max(x, max(forbidden)) + a + b
        while len(level) > 0:
            jump_times += 1
            next_level = set()
            for p in level:
                past_p.add(p[0])
                if p[0] - b > 0 and p[0] - b not in forbidden and p[0] - b not in past_p and not p[1]:
                    if p[0] - b == x:
                        return jump_times
                    next_level.add((p[0] - b,True))

                if p[0] + a not in forbidden and p[0] + a not in past_p:
                    if p[0] + a == x:
                        return jump_times
                    if p[0] > max_p:
                        return -1
                    next_level.add((p[0] + a, False))

            level = next_level
        return -1


if __name__ == '__main__':
    f = [162, 118, 178, 152, 167, 100, 40, 74, 199, 186, 26, 73, 200, 127, 30, 124, 193, 84, 184, 36, 103, 149, 153, 9, 54,
     154, 133, 95, 45, 198, 79, 157, 64, 122, 59, 71, 48, 177, 82, 35, 14, 176, 16, 108, 111, 6, 168, 31, 134, 164, 136,
     72, 98]
    aa = 29
    bb = 98
    xx = 80
    print(Solution().minimumJumps(f, aa, bb, xx))
