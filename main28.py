from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [f'{nums[0]}']
        start = nums[0]
        last_val = nums[0]
        result = []
        for index in range(1, len(nums)):
            if nums[index] == last_val+1:
                last_val = nums[index]
            else:
                if start == last_val:
                    result.append(f'{start}')
                else:
                    result.append(f'{start}->{last_val}')
                start = nums[index]
                last_val = start
        if start == last_val:
            result.append(f'{start}')
        else:
            result.append(f'{start}->{last_val}')

        return result





def main():
    nums = [0,2,3,4,6,8,9]
    print(Solution().summaryRanges(nums))


if __name__ == '__main__':
    main()
