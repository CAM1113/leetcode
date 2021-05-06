class Solution:
    def minimumTotal(self, triangle) -> int:
        result = [[0]]
        for i in range(len(triangle)):
            result.append([])
            for j in range(len(triangle[i])):
                if j - 1 < 0:
                    result[-1].append(result[-2][j] + triangle[i][j])
                    continue
                if j > len(triangle[i-1]) - 1:
                    result[-1].append(result[-2][j - 1] + triangle[i][j])
                    continue
                result[-1].append(min(result[-2][j - 1] + triangle[i][j], result[-2][j] + triangle[i][j]))
        return min(result[-1])


def main():
    x = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print(Solution().minimumTotal(x))


if __name__ == '__main__':
    main()
