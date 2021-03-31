class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        start = 0
        end = len(nums) - 1
        index = -1
        if nums[start] == target:
            index = start

        elif nums[end] == target:
            index = end
        else:
            while start < end - 1:
                middle = (start + end) // 2
                if nums[middle] == target:
                    index = middle
                    break
                if nums[middle] < target:
                    start = middle
                else:
                    end = middle

        if index == -1:
            return 0
        sub = 0
        while index - sub >= 0:
            if nums[index - sub] == target:
                sub += 1
            else:
                break
        sub -= 1
        add = 0
        while index + add < len(nums):
            if nums[index + add] == target:
                add += 1
            else:
                break
        add -= 1
        return add + sub + 1