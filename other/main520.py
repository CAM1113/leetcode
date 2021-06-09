class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) < 2:
            return True
        if "A" <= word[0] <= "Z":
            if "A" <= word[1] <= "Z":
                for c in word:
                    if not ("A" <= c <= "Z"):
                        return False
            else:
                for index in range(1, len(word)):
                    if not ("a" <= word[index] <= "z"):
                        return False
        else:
            for index in range(1, len(word)):
                if not ("a" <= word[index] <= "z"):
                    return False
        return True


if __name__ == '__main__':
    x = "usa"
    print(Solution().detectCapitalUse(x))
