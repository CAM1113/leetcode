class Solution:
    def titleToNumber(self, s: str) -> int:
        nums = 0
        start = ord('A') - 1
        for x in s:
            nums = nums * 26 + ord(x) - start
        return nums

if __name__ == '__main__':
    x = 'ZY'
    print(Solution().titleToNumber(x))