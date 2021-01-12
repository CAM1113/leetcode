def set_char(array, char, start, end):
    for i in range(start, end + 1):
        array[i] = char


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        start = 0
        state = '.'
        result = list(dominoes)
        for idx, s in enumerate(result):
            if s == '.':
                if idx < len(result) - 1:
                    continue
                else:
                    set_char(result, state, start, len(result) - 1)

            if s == 'L':
                if state == '.':
                    set_char(result, 'L', start, idx)
                    start = idx + 1
                    continue
                if state == 'R':
                    set_char(result, 'R', start, (start + idx) // 2)
                    set_char(result, 'L', (start + idx) // 2 + 1, idx)
                    if (start + idx) % 2 == 0:
                        result[(start + idx) // 2] = '.'
                    state = '.'
                    start = idx + 1

            if s == 'R':
                if state == '.':
                    start = idx
                    state = "R"
                    continue
                if state == 'R':
                    set_char(result, 'R', start, idx)
                    start = idx

        return ''.join(result)


if __name__ == '__main__':
    x = ".L.R...LR..L.."
    print(Solution().pushDominoes(x))
