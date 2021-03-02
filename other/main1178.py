from typing import List



class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        puzzle_chars = []
        puzzle_first_char = []
        words_chars = []
        for puzzle in puzzles:
            p = 0
            for c in puzzle:
                p = p | 1 << ord(c) - ord('a')
            puzzle_chars.append(p)

            p_first = 1 << ord(puzzle[0]) - ord('a')
            puzzle_first_char.append(p_first)

        for word in words:
            w = 0
            word = set(word)
            for c in word:
                w = w | 1 << ord(c) - ord('a')
            words_chars.append(w)
        index = 0
        result = []
        while index < len(puzzles):
            first_char = puzzle_first_char[index]
            puzzle_char = puzzle_chars[index]
            cnt = 0
            for w in words_chars:
                if w & first_char > 0 and (puzzle_char | w) ^ puzzle_char == 0:
                    cnt += 1
            result.append(cnt)
            index += 1
        return result


if __name__ == '__main__':
    words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"]
    puzzles = ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]
    print(Solution().findNumOfValidWords(words, puzzles))
