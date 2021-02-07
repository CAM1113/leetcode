class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        num_list = []
        while x != 0:
            num_list.append(x % 10)
            x = x // 10
        start = 0
        end = len(num_list) - 1
        while start <= end - 1:
            if num_list[start] != num_list[end]:
                return False
            start += 1
            end -= 1
        return True


if __name__ == '__main__':
    x = 1221
    print(Solution().isPalindrome(x))
