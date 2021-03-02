from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        char_num_dic = Counter(s)
        results = []
        start = 0
        end = 0
        if min(char_num_dic.values()) >= k:
            return len(s)
        while end < len(s) and start < len(s):
            if char_num_dic[s[end]] < k:
                if end - start >= k:
                    results.append(s[start:end])
                start = end + 1
                end = start
            else:
                end += 1
        results.append(s[start:end])
        max_length = 0
        for t in results:
            l = self.longestSubstring(t, k)
            if l > max_length:
                max_length = l
        return max_length


if __name__ == '__main__':
    s = "bbaaacbd"
    k = 3
    print(Solution().longestSubstring(s, k))
