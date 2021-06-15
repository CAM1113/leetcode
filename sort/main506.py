from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_index = []
        for index, val in enumerate(score):
            score_index.append((index, val))
        score_index.sort(key=lambda x: x[1], reverse=True)
        result = ["" for _ in range(len(score))]
        for i, (index, val) in enumerate(score_index):
            result[index] = f"{i + 1}"
        medal = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for i in range(3):
            if i < len(score):
                result[score_index[i][0]] = medal[i]
        return result
