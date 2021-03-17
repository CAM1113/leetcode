from typing import List


def area(r1, r2):
    max_w1 = max(r1[0], r2[0])
    max_h1 = max(r1[1], r2[1])
    min_w1 = min(r1[2], r2[2])
    min_h1 = min(r1[3], r2[3])
    w = max(0, min_w1 - max_w1)
    h = max(0, min_h1 - max_h1)
    return w * h


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        total_area = (rectangles[0][2] - rectangles[0][0]) * (rectangles[0][3] - rectangles[0][1])
        for i in range(1, len(rectangles)):
            total_area += (rectangles[i][2] - rectangles[i][0]) * (rectangles[i][3] - rectangles[i][1])
            for j in range(i):
                total_area -= area(rectangles[i], rectangles[j])
        return total_area % (10 ** 9 + 7)

if __na me__ == '__main__':
    nums = 0
    for i in range(1,11):
        for j in range(2,11):
            for k in range(3,11):
                if i + j + k == 11:
                    nums += 1
    print(nums)
