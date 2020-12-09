# KO
# 字符串匹配Boyer-Moore算法,只用了坏字符规则
def get_bad_position(needle, bad_char, bad_position):
    temp_bad_position = bad_position
    while bad_position > -1 and needle[bad_position] != bad_char:
        bad_position -= 1
    return temp_bad_position - bad_position


class Solution:
    def strStr(self, haystack: str, needle: str):
        # 坏字符规则，记录上一次出现的位置
        index = len(needle) - 1
        if len(needle) == 0:
            return 0
        if len(haystack) < len(needle):
            return -1
        while True:
            point = index
            while True:
                if haystack[point] == needle[-(index - point + 1)]:  # +1是python倒查的原因
                    point -= 1
                else:
                    # 计算后移位置,坏字符规则
                    shift_position1 = get_bad_position(needle, haystack[point], len(needle) - (index - point) - 1)
                    shift_position2 = get_good_position(needle,)
                    index += shift_position1
                    break

                if point == index - len(needle):
                    return point + 1
            if index >= len(haystack):
                return -1


def main():
    haystack = "mississippi"
    needle = "issip"
    inx = Solution().strStr(haystack, needle)
    print(inx)


if __name__ == '__main__':
    main()
