import collections


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        char_stack = []
        num_stack = []
        cnt = collections.defaultdict(int)
        index = 0
        while index < len(formula):
            c = formula[index]
            if "A" <= c <= "Z":
                char_start_index = index
                index += 1
                while index < len(formula) and "a" <= formula[index] <= "z":
                    index += 1
                char_end_index = index
                char = formula[char_start_index:char_end_index]
                num_start_index = index
                while index < len(formula) and "0" <= formula[index] <= "9":
                    index += 1
                num_end_index = index
                if num_start_index == num_end_index:
                    num = 1
                else:
                    num = int(formula[num_start_index:num_end_index])
                char_stack.append(char)
                num_stack.append(num)
                continue
            if c == "(":
                char_stack.append("(")
                index += 1
                continue
            if c == ")":
                index += 1
                num_start_index = index
                while index < len(formula) and "0" <= formula[index] <= "9":
                    index += 1
                num_end_index = index
                if num_start_index == num_end_index:
                    num = 1
                else:
                    num = int(formula[num_start_index:num_end_index])
                i = 1
                while char_stack[-i] != "(":
                    num_stack[-i] *= num
                    i += 1
                char_stack.pop(-i)
                continue
        for i in range(len(char_stack)):
            cnt[char_stack[i]] += num_stack[i]
        cn = list(cnt.items())
        cn.sort(key=lambda x: x[0])
        result = []
        for c, n in cn:
            if n == 1:
                result.append(c)
            else:
                result.append(f"{c}{n}")
        return "".join(result)


if __name__ == '__main__':
    print(Solution().countOfAtoms(formula="(H)"))
