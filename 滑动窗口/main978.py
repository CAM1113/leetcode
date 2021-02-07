from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        start = 0
        length = 1
        max_length = 1
        while start + length < len(arr):
            if arr[start] == arr[start + 1]:
                start += 1
                length = 1
                continue
            is_bigger = arr[start] > arr[start + 1]  # 偶大于奇
            if (length - 1) % 2 == 0:
                if is_bigger and arr[start + length - 1] > arr[start + length]:
                    # 符合要求
                    length += 1
                    if length > max_length:
                        max_length = length
                    continue
                if not is_bigger and arr[start + length - 1] < arr[start + length]:
                    # 符合要求
                    length += 1
                    if length > max_length:
                        max_length = length
                    continue
                start = start + length - 1
                length = 1

            else:
                if is_bigger and arr[start + length - 1] < arr[start + length]:
                    # 符合要求
                    length += 1
                    if length > max_length:
                        max_length = length
                    continue
                if not is_bigger and arr[start + length - 1] > arr[start + length]:
                    # 符合要求
                    length += 1
                    if length > max_length:
                        max_length = length
                    continue
                start = start + length - 1
                length = 1

        return max_length


if __name__ == '__main__':
    x = [4,8,12,16]
    print(Solution().maxTurbulenceSize(x))
