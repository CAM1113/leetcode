from typing import List


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        index = 0
        length = len(s) - 1
        while index < length - index:
            temp = s[index]
            s[index] = s[length - index]
            s[length - index] = temp
            index += 1
        start = 0
        end = 0
        while start < len(s):
            while end < len(s) and s[end] != " ":
                end += 1
            index = 0
            end -= 1
            while start + index < end - index:
                temp = s[start + index]
                s[start + index] = s[end - index]
                s[end - index] = temp
                index += 1
            end += 2
            start = end


if __name__ == '__main__':
    x = ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]
    print(Solution().reverseWords(x))
