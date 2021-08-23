import collections


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = collections.deque()
        results = []
        index = 0
        for c in s:
            if index < k:
                result.appendleft(c)
                index += 1
                continue
            if index < 2 * k:
                result.append(c)
                index += 1
                if index == 2*k:
                    index = 0
                    for r in result:
                        results.append(r)
                    result.clear()

        for r in result:
            results.append(r)
        return "".join(results)


if __name__ == '__main__':
    print(Solution().reverseStr("abcdefg", 2))
