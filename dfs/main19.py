from typing import List


def dfs(digits, index, result, results, num_dic):
    if len(result) == len(digits):
        results.append(''.join(result))
        return
    d = int(digits[index])
    s_index = num_dic[d]
    for s in s_index:
        result.append(s)
        dfs(digits, index + 1, result, results, num_dic)
        result.pop()


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        num_dic = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        index = 0
        result = []
        results = []
        dfs(digits, index, result, results, num_dic)
        return results


def main():
    digits = "23"
    print(Solution().letterCombinations(digits))


if __name__ == '__main__':
    main()
