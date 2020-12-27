import sys
class Solution:
    def threeSum(self, nums):
        triples = []
        nums.sort()
        last_val = sys.maxsize
        for i in range(len(nums) - 2):
            target = nums[i]
            if target > 0:
                break
            if target == last_val:
                continue
            last_val = target
            start = i + 1
            end = len(nums) - 1
            while start < end:
                if nums[start] + nums[end] == -target:
                    triples.append([target, nums[start], nums[end]])
                    temp = nums[start]
                    while nums[start] == temp and start < end:
                        start += 1
                    temp = nums[end]
                    while nums[end] == temp and start < end:
                        end -= 1
                    continue
                if nums[start] + nums[end] < -target:
                    temp = nums[start]
                    while nums[start] == temp and start < end:
                        start += 1
                    continue
                if nums[start] + nums[end] > -target:
                    temp = nums[end]
                    while nums[end] == temp and start < end:
                        end -= 1
                    continue
        return triples


def main():
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums))


if __name__ == '__main__':
    main()
