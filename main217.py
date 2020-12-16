class Solution:
    def containsDuplicate(self, nums) -> bool:
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False


def main():
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(Solution().containsDuplicate(nums))


if __name__ == '__main__':
    main()
