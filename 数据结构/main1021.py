class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        li = []
        result = ''
        start = 0
        for index, c in enumerate(S):
            if c == '(':
                li.append(c)
            if c == ')':
                li.pop()
                if len(li) == 0:
                    result += S[start + 1:index]
                    start = index + 1
        return result
