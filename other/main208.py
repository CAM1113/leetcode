class Trie:

    def __init__(self):
        self.dict = {}

    def insert(self, word: str) -> None:
        dic = self.dict
        for index, c in enumerate(word):
            if c in dic.keys():
                element = dic[c]
                if index == len(word) - 1:
                    element[1] = True
                    return
                else:
                    dic = element[0]
            else:
                dic[c] = [{}, False]
                element = dic[c]
                if index == len(word) - 1:
                    element[1] = True
                    return
                else:
                    dic = element[0]

    def search(self, word: str) -> bool:
        dic = self.dict
        element = [{}, False]
        for c in word:
            if c in dic.keys():
                element = dic[c]
                dic = element[0]
            else:
                return False
        return element[1]

    def startsWith(self, prefix: str) -> bool:
        dic = self.dict
        for c in prefix:
            if c in dic.keys():
                element = dic[c]
                dic = element[0]
            else:
                return False
        return True

if __name__ == '__main__':
    t = Trie()

    t.insert("apple")
