from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prefix_sum = [0]
        pre = 0
        for a in arr:
            pre += a
            prefix_sum.append(pre)
        length = 1
        result = 0
        while length <= len(arr):
            start = 0
            while start + length <= len(arr):
                result += prefix_sum[start+length] - prefix_sum[start]
                start += 1
            length += 2
        return result

if __name__ == '__main__':
    x = [1,4,2,5,3]
    print(Solution().sumOddLengthSubarrays(x))
