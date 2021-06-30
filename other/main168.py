class Solution:
    def convertToTitle(self, n: int) -> str:
        num_list = []
        while n > 0:
            n -= 1
            num_list.append(n % 26)
            n //= 26
        return "".join([chr(x + ord("A")) for x in num_list[::-1]])


if __name__ == '__main__':
    x = 28
    print(Solution().convertToTitle(x))
