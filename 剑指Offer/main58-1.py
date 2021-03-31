class Solution:
    def reverseWords(self, s: str) -> str:
        character = []
        result = []
        for c in s:
            if c == ' ':
                if len(character) == 0:
                    continue
                else:
                    result.append(''.join(character))
                    character = []
            else:
                character.append(c)
        if len(character) != 0:
            result.append(''.join(character))
        return ' '.join(result[::-1])