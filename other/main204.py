import math
def is_prim(num):
    if num == 1 or num == 4:
        return False
    if num == 2 or num == 3 or num == 5:
        return True

    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        return False
    end = math.ceil(math.sqrt(num)) + 1
    for i in range(1, end, 2):
        if i == 1:
            continue
        if num % i == 0:
            return False
    return True


class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        for i in range(1, n):
            if is_prim(i):
                count += 1
        return count