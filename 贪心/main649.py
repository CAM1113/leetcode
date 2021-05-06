def is_over(s):
    m = s[0]
    for c in s:
        if c != m:
            return True
    return False


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        numD = 0
        numR = 0
        while len(senate) > 1 and is_over(senate):
            if senate[0] == "D" and numR == 0:
                numD += 1
                senate = senate[1:]
                senate = senate + "D"
            if senate[0] == "R" and numD == 0:
                numR += 1
                senate = senate[1:]
                senate = senate + "R"

            if senate[0] == "D" and numR != 0:
                numR -= 1
                senate = senate[1:]

            if senate[0] == "R" and numD != 0:
                numD -= 1
                senate = senate[1:]

        if senate[0] == "D":
            return "Dire"
        else:
            return "Radiant"


def main():
    l = "RRR"
    print(Solution().predictPartyVictory(l))


if __name__ == '__main__':
    main()
