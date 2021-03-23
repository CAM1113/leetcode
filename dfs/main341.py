class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> [NestedInteger]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

def dfs(arr:[NestedInteger], array):
    for a in arr:
        if a.isInteger():
            array.append(a.getInteger())
        else:
            dfs(a.getList(), array)


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.array = []
        dfs(nestedList,self.array)
        self.length = 0

    def next(self) -> int:
        v = self.array[self.length]
        self.length += 1
        return v

    def hasNext(self) -> bool:
        return self.length < len(self.array)