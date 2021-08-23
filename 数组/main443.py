from typing import List


def get_cnt(n):
    if n == 1:
        return 1
    elif n < 10:
        return 2
    elif n < 100:
        return 3
    elif n < 1000:
        return 4
    else:
        return 5


class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 1
        result = 0
        last_char = chars[0]
        cnt = 1
        chars_index = 0
        while index < len(chars):
            if chars[index] == last_char:
                cnt += 1
                index += 1
                continue
            else:
                chars[chars_index] = last_char
                chars_index += 1
                if cnt == 1:
                    last_char = chars[index]
                    index += 1
                    continue
                char_cnt = []
                while cnt > 0:
                    char_cnt.append(str(cnt % 10))
                    cnt //= 10
                char_cnt = char_cnt[::-1]
                for c in char_cnt:
                    chars[chars_index] = c
                    chars_index += 1
                last_char = chars[index]
                index += 1
                cnt = 1
                continue
        chars[chars_index] = last_char
        chars_index += 1
        if cnt == 1:
            return chars_index

        char_cnt = []
        while cnt > 0:
            char_cnt.append(str(cnt % 10))
            cnt //= 10
        char_cnt = char_cnt[::-1]
        for c in char_cnt:
            chars[chars_index] = c
            chars_index += 1

        return chars_index
