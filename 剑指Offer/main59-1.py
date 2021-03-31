from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        start = 0
        end = k
        lis = nums[:k]
        lis.sort(reverse=True)
        result = [lis[0]]
        while end < len(nums):
            if nums[end] < lis[0]:
                lis.append(nums[end])
            else:
                lis.insert(0, nums[end])
            end += 1

            if nums[start] == lis[0]:
                lis.remove(nums[start])
                lis.sort(reverse=True)
            else:
                lis.remove(nums[start])
            start += 1
            result.append(lis[0])

        return result


if __name__ == '__main__':
    x = [7, 2, 4]
    print(Solution().maxSlidingWindow(x, 2))
