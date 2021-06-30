class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        num_lis = []
        minus = 1
        if num < 0:
            minus = -1
            num *= -1
        while num > 0:
            num_lis.append(num % 7)
            num //= 7
        if minus < 0:
            num_lis.append("-")
        return "".join([f"{x}" for x in num_lis[::-1]])
