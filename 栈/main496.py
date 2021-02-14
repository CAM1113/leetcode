from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        start = 0
        res_dic = {}
        while start < len(nums2):
            if len(stack) == 0 or nums2[start] < stack[-1]:
                stack.append(nums2[start])
                start += 1
                continue
            while len(stack) > 0 and nums2[start] > stack[-1]:
                res_dic[stack[-1]] = nums2[start]
                stack.pop()
            stack.append(nums2[start])
            start += 1
        re = []
        for key in nums1:
            if key in res_dic.keys():
                re.append(res_dic[key])
            else:
                re.append(-1)
        return re


if __name__ == '__main__':
    n1 = [4, 1, 2]
    n2 = [1, 3, 4, 2]
    print(Solution().nextGreaterElement(n1, n2))
