class Solution:
    def isValid(self, s: str) -> bool:
        li = []
        for c in s:
            if len(li) == 0 or c == '(' or c == '[' or c == '{':
                li.append(c)
            elif c == ')':
                if li[-1] != '(':
                    return False
                else:
                    li.pop()
            elif c == ']':
                if li[-1] != '[':
                    return False
                else:
                    li.pop()
            elif c == '}':
                if li[-1] != '{':
                    return False
                else:
                    li.pop()
        return len(li) == 0



if __name__ == '__main__':
    ss = "()[]{}"
    print(Solution().isValid(ss))