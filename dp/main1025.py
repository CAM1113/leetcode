class Solution:
    def divisorGame(self, N: int) -> bool:
        if N == 1:
            return False
        if N == 2:
            return True
        state = [False] * (N + 1)
        state[2] = True
        for i in range(3, N + 1):
            for j in range(1, i):
                if i % j == 0 and state[j]:
                    state[i] = True
                    break
        return state[-1]


if __name__ == '__main__':
    x = 6
    print(Solution().divisorGame(x))
