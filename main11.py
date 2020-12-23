class Solution:
    def maxArea(self, height) -> int:
        s = 0
        e = len(height) - 1
        max_area = -1
        while e > s:
            a = (e - s) * min(height[e], height[s])
            if a > max_area:
                max_area = a
            if height[e] > height[s]:
                s += 1
            else:
                e -= 1
        return max_area


if __name__ == '__main__':
    hs = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(Solution().maxArea(hs))
