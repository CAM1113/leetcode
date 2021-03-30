def is_move(num_dic: dict, k):
    sum_num = sum(num_dic.values())
    if sum_num <= 1:
        return False
    max_val = max(num_dic.values())
    if sum_num - max_val > k:
        return True
    return False


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        length = 0
        num_dic = {}
        while start + length < len(s):
            if s[start + length] in num_dic:
                num_dic[s[start + length]] += 1
            else:
                num_dic[s[start + length]] = 1
            if is_move(num_dic, k):
                num_dic[s[start]] -= 1
                start += 1
            else:
                length += 1
        return length


if __name__ == '__main__':
    s = "ABAB"
    k = 2
    print(Solution().characterReplacement(s, k))
