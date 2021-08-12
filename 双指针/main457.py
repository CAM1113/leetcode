from typing import List


def find_cycle(nums: List[int], start: int):
    n = len(nums)
    slow = start
    fast = (start + nums[start]) % n
    fast = (fast + nums[fast]) % n
    while slow != fast:
        slow = (slow + nums[slow]) % n
        fast = (fast + nums[fast]) % n
        fast = (fast + nums[fast]) % n

    start = slow
    length = 1
    slow = (slow + nums[slow]) % n
    while slow != start:
        length += 1
        if nums[slow] * nums[start] < 0:
            return False
        slow = (slow + nums[slow]) % n
    if length > 1:
        return True
    return False


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            if find_cycle(nums, i):
                return True
        return False


if __name__ == '__main__':
    nums = [2, 2, 2, 2, 2, 4, 7]
    print(Solution().circularArrayLoop(nums))
