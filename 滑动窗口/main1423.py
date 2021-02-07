from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)
        length = len(cardPoints) - k
        min_sums = sum(cardPoints[:length])
        sums = min_sums
        total = sums
        start = 0
        while start + length < len(cardPoints):
            total += cardPoints[start + length]
            sums -= cardPoints[start]
            sums += cardPoints[start + length]
            if sums < min_sums:
                min_sums = sums
            start += 1
        return total - min_sums


if __name__ == '__main__':
    x = [100,40,17,9,73,75]
    k = 3
    print(Solution().maxScore(x, k))
