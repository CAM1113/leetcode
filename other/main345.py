class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        start = 0
        end = len(s) - 1
        reverse_set = {'a', 'e', 'i', 'o', 'u','A','E','I','O','U'}
        while start < end:
            while start < end and s[start] not in reverse_set:
                start += 1
            while start < end and s[end] not in reverse_set:
                end -= 1
            if start >= end:
                break
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1
        return "".join(s)