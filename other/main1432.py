class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        max_val = -1
        min_val = num
        for i in range(10):
            for j in range(10):
                ss = s.replace(f"{i}", f"{j}")
                if j == 0 and ss[0] == "0":
                    continue
                ss = int(ss)
                if ss > max_val:
                    max_val = ss
                if ss < min_val:
                    min_val = ss
        return max_val - min_val
