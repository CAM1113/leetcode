# 1286. 字母组合迭代器

# 请你设计一个迭代器类，包括以下内容：
# 
# 一个构造函数，输入参数包括：一个有序且字符唯一的字符串characters（该字符串只包含小写英文字母）和一个数字combinationLength。
# 函数next()，按字典序返回长度为combinationLength 的下一个字母组合。
# 函数hasNext()，只有存在长度为combinationLength 的下一个字母组合时，才返回True；否则，返回 False。
# 
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/iterator-for-combination
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class CombinationIterator:

    def __init__(self, characters, combinationLength: int):
        self.characters = characters
        self.length = combinationLength
        self.mask = [i for i in range(self.length)]
        self.has_next = True

    def next(self) -> str:
        pass

    def hasNext(self) -> bool:
        pass

    def add_one(self, index):
        self.mask[index] += 1
        if self.mask[index] == len(self.characters) + index:
            self.mask[index] = self.mask[index - 1]
            self.add_one(index - 1)
