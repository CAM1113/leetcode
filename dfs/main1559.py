# 1559. 二维网格图中探测环

def dfs(matrix, is_used, currentX, currentY, lastX, lastY):
    is_used[currentX][currentY] = True
    val = matrix[currentX][currentY]
    if currentX > 0 and (currentX - 1 != lastX or currentY != lastY) \
            and matrix[currentX - 1][currentY] == val:
        if is_used[currentX - 1][currentY]:
            return True
        if dfs(matrix, is_used, currentX - 1, currentY, currentX, currentY):
            return True

    if currentX + 1 < len(matrix) and (currentX + 1 != lastX or currentY != lastY) \
            and matrix[currentX + 1][currentY] == val:
        if is_used[currentX + 1][currentY]:
            return True
        if dfs(matrix, is_used, currentX + 1, currentY, currentX, currentY):
            return True

    if currentY>0 and (currentX != lastX or currentY - 1 != lastY) \
            and matrix[currentX][currentY - 1] == val:
        if is_used[currentX][currentY - 1]:
            return True
        if dfs(matrix, is_used, currentX, currentY - 1, currentX, currentY):
            return True

    if currentY + 1 < len(matrix[0]) and (currentX != lastX or currentY + 1 != lastY) \
            and matrix[currentX][currentY + 1] == val:
        if is_used[currentX][currentY + 1]:
            return True
        if dfs(matrix, is_used, currentX, currentY + 1, currentX, currentY):
            return True


class Solution:
    def containsCycle(self, grid) -> bool:
        is_used = [[False for _ in grid[0]] for _ in grid]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if is_used[i][j]:
                    continue
                if dfs(grid,is_used,i,j,i,j):
                    return True
        return False



def main():
    grid = [["a", "a", "a", "a"], ["a", "b", "b", "a"], ["a", "b", "b", "a"], ["a", "a", "a", "a"]]
    print(Solution().containsCycle(grid))


if __name__ == '__main__':
    main()
