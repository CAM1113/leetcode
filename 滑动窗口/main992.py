from typing import List


class Solution:
    def subarraysWithKDis tinct(self, A: List[int], K: int) -> int:
        start = 0
        length = 0
        cnt_dic = {}
        results = 0
        while start + length < len(A):
            while start + length < len(A) and len(cnt_dic.keys()) <= K:
                if A[start + length] in cnt_dic.keys():
                    cnt_dic[A[start + length]] += 1
                else:
                    cnt_dic[A[start + length]] = 1
                if len(cnt_dic) == K:
                    results += 1
                length += 1
            cnt_dic[A[start]] -= 1
            if cnt_dic[A[start]] == 0:
                del cnt_dic[A[start]]


            start += 1.
            length = 0
            cnt_dic = {}

        return results


if __name__ == '__main__':
    x = [1, 2, 1, 2, 3]
    kk = 2
    print(Solution().subarraysWithKDistinct(x, kk))
