from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        result = []
        val = 0
        for i in A:
            val = val * 2 + i
            if val % 5 == 0:
                result.append(True)
            else:
                result.append(False)
        return result


def main():
    a = []
    print(Solution().prefixesDivBy5(a))


if __name__ == '__main__':
    # main()
    x = 0
    print(x << 1)
