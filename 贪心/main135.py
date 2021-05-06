class Solution:
    def candy(self, ratings) -> int:
        nums = [1 for _ in ratings]
        for idx in range(len(nums)):
            if idx == 0:
                continue
            if ratings[idx] > ratings[idx - 1] and nums[idx] <= nums[idx-1]:
                nums[idx] = nums[idx - 1] + 1

        for idx in range(len(nums) - 1, -1, -1):
            if idx == len(nums) - 1:
                continue
            if ratings[idx] > ratings[idx + 1] and nums[idx] <= nums[idx + 1]:
                nums[idx] = nums[idx + 1] + 1

        return sum(nums)


def main():
    c = [1, 0, 2]
    print(Solution().candy(c))


if __name__ == '__main__':
    main()
