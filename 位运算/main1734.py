from typing import List


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        all_xor = 0
        for i in range(1, len(encoded) + 2):
            all_xor ^= i

        all_xor_except_0 = 0
        for i in range(1, len(encoded), 2):

            all_xor_except_0 ^= encoded[i]

        first = all_xor_except_0 ^ all_xor
        result = [first]
        for i in encoded:
            result.append(result[-1] ^ i)
        return result


if __name__ == '__main__':
    x = [6, 5, 4, 6]
    print(Solution().decode(x))
