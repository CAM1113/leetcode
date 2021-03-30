class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        start = 0
        length = 0
        max_length = 0
        char_set = {}
        while start + length < len(s):
            if s[start + length] in char_set.keys() and start <= char_set[s[start + length]] < start + length:
                len_temp = length
                length = start + length - char_set[s[start + length]] - 1
                start = char_set[s[start + len_temp]] + 1
            char_set[s[start + length]] = start + length
            length += 1
            if length > max_length:
                max_length = length
        return max_length
