from typing import List


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.tree = [kingName, True, []]
        self.info = {kingName: self.tree}

    def birth(self, parentName: str, childName: str) -> None:
        node = [childName, True, []]
        self.info[parentName][2].append(node)
        self.info[childName] = node

    def death(self, name: str) -> None:
        self.info[name][1] = False

    def getInheritanceOrder(self) -> List[str]:
        stack = [self.tree]
        result = []
        while len(stack) != 0:
            node = stack.pop()
            if node[1]:
                result.append(node[0])
            stack += node[2][::-1]
        return result
