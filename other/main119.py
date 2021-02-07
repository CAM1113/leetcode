from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        last_row = [1, 1]
        if rowIndex == 1:
            return last_row

        for i in range(2, rowIndex + 1):
            result = []
            for j in range(i + 1):
                if j == 0:
                    result.append(1)
                    continue
                if j == i:
                    result.append(1)
                    continue
                result.append(last_row[j] + last_row[j - 1])
            last_row = result
        return last_row
