from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        K_list = []
        while K != 0:
            K_list.append(K % 10)
            K = K // 10
        K = K_list[::-1]
        if len(K) > len(A):
            temp = A
            A = K
            K = temp

        index = 1
        add = 0
        while index <= len(K):
            temp = K[-index] + A[-index] + add
            if temp >= 10:
                add = 1
                temp = temp % 10
            else:
                add = 0
            A[-index] = temp
            index += 1
        while index <= len(A):
            temp = A[-index] + add
            if temp >= 10:
                add = 1
                temp = temp % 10
            else:
                add = 0
            A[-index] = temp
            index += 1
        if add == 1:
            A.insert(0,1)
        return A



def main():
    A = [0]
    K = 1
    print(Solution().addToArrayForm(A, K))


if __name__ == '__main__':
    main()
