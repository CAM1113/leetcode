class Solution:
    def simplifyPath(self, path: str) -> str:
        result = []
        paths = path.split('/')
        for c in paths:
            if c == "" or c == ".":
                continue
            if c == "..":
                if len(result) != 0:
                    result.pop()
                continue
            result.append(c)
        path = "/"
        for c in result:
            path += c + "/"
        if len(path) > 1:
            path = path[:-1]
        return path


if __name__ == '__main__':
    p = "/a/./b/../../c/"
    print(Solution().simplifyPath(p))
