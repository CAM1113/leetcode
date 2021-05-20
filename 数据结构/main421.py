from typing import List


class TreeNode:
    def __init__(self):
        self.val = 0
        self.left = None
        self.right = None


def get_01(n: int):
    s = [0] * 31
    index = 0
    while n > 0:
        if n % 2 == 1:
            s[index] = 1
        n //= 2
        index += 1
    return ''.join([str(x) for x in s[::-1]])


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        root = TreeNode()
        str_list = []
        for n in nums:
            s = get_01(n)
            str_list.append(s)
            r = root
            for c in s:
                if c == '0':
                    if r.left is None:
                        r.left = TreeNode()
                    r = r.left
                else:
                    if r.right is None:
                        r.right = TreeNode()
                    r = r.right
            r.val = n
        max_xor = 0

        for index in range(len(str_list)):
            s = str_list[index]
            n = nums[index]
            r = root
            for c in s:
                if c == "0":
                    if r.right is None:
                        r = r.left
                    else:
                        r = r.right
                else:
                    if r.left is None:
                        r = r.right
                    else:
                        r = r.left
            xor = n ^ r.val
            if xor > max_xor:
                max_xor = xor
        return max_xor


if __name__ == '__main__':
    x =[14,70,53,83,49,91,36,80,92,51,66,70]
    print(Solution().findMaximumXOR(x))
