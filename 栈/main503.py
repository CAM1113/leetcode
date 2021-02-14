from typing import List


def is_full(stack):
    ii = stack[-1][1]
    for i in range(len(stack) - 1):
        if stack[i][1] == ii:
            return True
    return False


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        start = 0
        result_dic = [-1 for _ in range(len(nums))]
        is_used = [False for _ in range(len(nums))]
        stack = []
        rest_num = len(nums)
        num_step = 0
        while rest_num > 1 and num_step < len(nums) * 2:
            num_step += 1
            if len(stack) == 0 or stack[-1][0] >= nums[start]:
                stack.append([nums[start], start])
                start = (start + 1) % len(nums)
                if len(stack) >= len(nums) and is_full(stack):
                    return result_dic
                continue
            while len(stack) > 0 and stack[-1][0] < nums[start]:
                if is_used[stack[-1][1]] == False:
                    result_dic[stack[-1][1]] = nums[start]
                    is_used[stack[-1][1]] = True
                    rest_num -= 1
                stack.pop()
            stack.append([nums[start], start])
            start = (start + 1) % len(nums)
        return result_dic


if __name__ == '__main__':
    x = [-6, -1, 5, 4, 1, -8, 6, 7, -3, 6, 0, -6, -7, 8, -8, -4, 1]
    print(Solution().nextGreaterElements(x))
