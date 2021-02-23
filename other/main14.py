from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        index = 0
        while True:
            if index >= len(strs[0]):
                return strs[0]
            c = strs[0][index]
            for s in strs:
                if index >= len(s):
                    return s
                if s[index] == c:
                    continue
                else:
                    return strs[0][:index]
            index += 1
