class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        short_num = num1
        long_num = num2
        if len(short_num) > len(long_num):
            long_num, short_num = short_num, long_num
        index = 0
        add = 0
        result = []
        zero = ord("0")
        while index < len(short_num):
            su = (ord(short_num[index])-zero) + (ord(long_num[index])-zero) + add
            result.append(su % 10)
            add = su // 10
            index += 1
        while index < len(long_num):
            su = ord(long_num[index]) - zero + add
            result.append(su % 10)
            add = su // 10
            index += 1
        if add > 0:
            result.append(add)
        result = result[::-1]
        return "".join([str(i) for i in result])


if __name__ == '__main__':
    x = "11"
    y = "123"
    print(Solution().addStrings(x, y))
