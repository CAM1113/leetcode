def get_str(n, one, five, ten):
    result = ""
    if n == 4:
        result += f"{one}{five}"
    elif n == 9:
        result += f"{one}{ten}"
    else:
        if n >= 5:
            result += f"{five}"
            n -= 5
        for i in range(n):
            result += f"{one}"


class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        n = num // 1000
        for i in range(n):
            result += "M"
        num %= 1000
        n = num // 100
        result += get_str(n, "C", "D", "M")
        num %= 100
        n = num // 10
        result += get_str(n, "X", "L", "C")
        num %= 10
        result += get_str(num, "I", "V", "X")
        return result
