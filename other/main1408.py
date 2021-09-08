from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        words.sort(key=lambda x: len(x))
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i] in words[j]:
                    result.append(words[i])
        return result
