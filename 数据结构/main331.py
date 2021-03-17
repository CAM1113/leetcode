class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        ss = preorder.split(",")
        stack = []
        for c in ss:
            if c == '#':
                while len(stack) > 0 and stack[-1] == "#":
                    stack.pop()
                    if len(stack) > 0:
                        stack.pop()
                    else:
                        return False
                stack.append("#")
            else:
                stack.append(c)
        return len(stack) == 1 and stack[-1] == "#"


if __name__ == '__main__':
    x = "9,#,#,1"
    print(Solution().isValidSerialization(x))
