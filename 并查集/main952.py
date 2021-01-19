import math
from typing import List


def is_one(x1, x2):
    min_val = min(x1, x2)
    for i in range(2, min_val + 1):
        if x1 % i == 0 and x2 % i == 0:
            return True
    return False


zs = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
      109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233,
      239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373,
      379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509,
      521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659,
      661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823,
      827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983,
      991, 997]


def get_all_mul(x):
    re = set([])
    d = zs[0]
    index = 0
    while d <= x and index < len(zs):
        if x % d == 0:
            while x % d == 0:
                x /= d
            re.add(d)
        d = zs[index]
        index += 1
    return re


class Solution:

    def find(self, array, index):
        if array[index] == index:
            return index
        root = self.find(array, array[index])
        array[index] = root
        return root

    def union(self, array, index1, index2):
        root1 = self.find(array, index1)
        root2 = self.find(array, index2)
        array[root2] = root1

    def largestComponentSize(self, A: List[int]) -> int:
        array = [i for i in range(len(A))]
        mul_dic = {}
        for i in range(len(A)):
            mul_dic[i] = get_all_mul(A[i])

        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                root1 = self.find(array, i)
                root2 = self.find(array, j)
                if root2 == root1:
                    continue
                set1 = mul_dic[root1]
                set2 = mul_dic[root2]
                for el in set2:
                    if el in set1:
                        array[root2] = root1
                        set1 = set1.union(set2)
                        mul_dic[root1] = set1
                        del mul_dic[root2]
                        break

        num_dic = {}
        for i in range(len(A)):
            root = self.find(array, i)
            if root in num_dic.keys():
                num_dic[root] += 1
            else:
                num_dic[root] = 1
        return max(num_dic.values())


def main():
    x = [2, 7, 522, 526, 535, 26, 944, 35, 519, 45, 48, 567, 266, 68, 74, 591, 81, 86, 602, 93, 610, 621, 111, 114, 629,
         641, 131, 651, 142, 659, 669, 161, 674, 163, 180, 187, 190, 194, 195, 206, 207, 218, 737, 229, 240, 757, 770,
         260, 778, 270, 272, 785, 274, 290, 291, 292, 296, 810, 816, 314, 829, 833, 841, 349, 880, 369, 147, 897, 387,
         390, 905, 405, 406, 407, 414, 416, 417, 425, 938, 429, 432, 926, 959, 960, 449, 963, 966, 929, 457, 463, 981,
         985, 79, 487, 1000, 494, 508]
    print(Solution().largestComponentSize(x))


if __name__ == '__main__':
    main()
    # print(is_one(15, 6))
