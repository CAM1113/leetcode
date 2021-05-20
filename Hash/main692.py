from collections import Counter
from typing import List, Tuple


class Heap:
    def __init__(self, k):
        self.length = k
        self.already_len = 0
        self.heap = [(-1, "z")] * k

    def is_larger(self, x: Tuple[int, str], y: Tuple[int, str]):
        if x[0] > y[0]:
            return True
        if x[0] < y[0]:
            return False
        return x[1] < y[1]

    def add(self, x: Tuple[int, str]):
        if self.is_larger(x, self.heap[0]):
            self.heap[0] = x
            index = 0
            while index < self.length:
                min_index = index
                if index * 2 + 1 < self.length and self.is_larger(self.heap[min_index], self.heap[index * 2 + 1]):
                    min_index = index * 2 + 1
                if index * 2 + 2 < self.length and self.is_larger(self.heap[min_index], self.heap[index * 2 + 2]):
                    min_index = index * 2 + 2
                if min_index == index:
                    break
                temp = self.heap[min_index]
                self.heap[min_index] = self.heap[index]
                self.heap[index] = temp
                index = min_index

    def get_head(self):
        result = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        index = 0
        while index < len(self.heap):
            min_index = index
            if index * 2 + 1 < len(self.heap) and self.is_larger(self.heap[min_index], self.heap[index * 2 + 1]):
                min_index = index * 2 + 1
            if index * 2 + 2 < len(self.heap) and self.is_larger(self.heap[min_index], self.heap[index * 2 + 2]):
                min_index = index * 2 + 2
            if min_index == index:
                break
            temp = self.heap[min_index]
            self.heap[min_index] = self.heap[index]
            self.heap[index] = temp
            index = min_index
        return result


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        cnt = Counter(words)
        print(cnt)
        h = Heap(k)

        for k in cnt.keys():
            h.add((cnt[k], k))
        result = []
        print(h.heap)
        while len(h.heap) > 0:
            result.append(h.get_head()[1])
        return result[::-1]


if __name__ == '__main__':
    x = ["glarko", "zlfiwwb", "nsfspyox", "pwqvwmlgri", "qggx", "qrkgmliewc", "zskaqzwo", "zskaqzwo", "ijy",
         "htpvnmozay", "jqrlad", "ccjel", "qrkgmliewc", "qkjzgws", "fqizrrnmif", "jqrlad", "nbuorw", "qrkgmliewc",
         "htpvnmozay", "nftk", "glarko", "hdemkfr", "axyak", "hdemkfr", "nsfspyox", "nsfspyox", "qrkgmliewc", "nftk",
         "nftk", "ccjel", "qrkgmliewc", "ocgjsu", "ijy", "glarko", "nbuorw", "nsfspyox", "qkjzgws", "qkjzgws",
         "fqizrrnmif", "pwqvwmlgri", "nftk", "qrkgmliewc", "jqrlad", "nftk", "zskaqzwo", "glarko", "nsfspyox",
         "zlfiwwb", "hwlvqgkdbo", "htpvnmozay", "nsfspyox", "zskaqzwo", "htpvnmozay", "zskaqzwo", "nbuorw", "qkjzgws",
         "zlfiwwb", "pwqvwmlgri", "zskaqzwo", "qengse", "glarko", "qkjzgws", "pwqvwmlgri", "fqizrrnmif", "nbuorw",
         "nftk", "ijy", "hdemkfr", "nftk", "qkjzgws", "jqrlad", "nftk", "ccjel", "qggx", "ijy", "qengse", "nftk",
         "htpvnmozay", "qengse", "eonrg", "qengse", "fqizrrnmif", "hwlvqgkdbo", "qengse", "qengse", "qggx", "qkjzgws",
         "qggx", "pwqvwmlgri", "htpvnmozay", "qrkgmliewc", "qengse", "fqizrrnmif", "qkjzgws", "qengse", "nftk",
         "htpvnmozay", "qggx", "zlfiwwb", "bwp", "ocgjsu", "qrkgmliewc", "ccjel", "hdemkfr", "nsfspyox", "hdemkfr",
         "qggx", "zlfiwwb", "nsfspyox", "ijy", "qkjzgws", "fqizrrnmif", "qkjzgws", "qrkgmliewc", "glarko", "hdemkfr",
         "pwqvwmlgri"]
    k = 14
    print(Solution().topKFrequent(x, k))
