from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        result = 0
        for i in range(len(arr)):
            zero_list = [i]
            xor_sum = 0
            index = i
            while index < len(arr):
                xor_sum ^= arr[index]
                if xor_sum == 0:
                    zero_list.append(index)
                index += 1
            for ii in range(len(zero_list)):
                result += zero_list[ii] - zero_list[0]
        return result


if __name__ == '__main__':
    x =  [7,11,12,9,5,2,7,17,22]
    print(Solution().countTriplets(x))
