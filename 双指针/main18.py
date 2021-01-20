from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)-3):
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            for j in range(i + 1, len(nums)-2):
                if j > i+1 and nums[j - 1] == nums[j]:
                    continue
                target_ij = target - nums[i] - nums[j]
                min_index = j + 1
                max_index = len(nums) - 1
                while min_index < max_index:
                    if nums[max_index] + nums[min_index] == target_ij:
                        result.append([nums[i], nums[j], nums[min_index], nums[max_index]])
                        temp = nums[min_index]
                        while min_index < max_index and nums[min_index] == temp:
                            min_index += 1
                        temp = nums[max_index]
                        while min_index < max_index and nums[max_index] == temp:
                            max_index -= 1
                    elif nums[max_index] + nums[min_index] < target_ij:
                        temp = nums[min_index]
                        while min_index < max_index and nums[min_index] == temp:
                            min_index += 1
                    elif min_index < max_index and nums[max_index] + nums[min_index] > target_ij:
                        temp = nums[max_index]
                        while nums[max_index] == temp:
                            max_index -= 1
        return result


def main():
    n =[-2,-1,-1,1,1,2,2]
    t = 0
    print(Solution().fourSum(n, t))

if __name__ == '__main__':
    main()
