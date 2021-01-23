class Solution:
    def groupAnagrams(self, strs):
        if len(strs) == 0:
            return []
        sort_dict = {}
        for s in strs:
            order_s = ''.join(sorted(s))
            if order_s in sort_dict.keys():
                sort_dict[order_s].append(s)
            else:
                sort_dict[order_s] = [s]
        return list(sort_dict.values())


def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))


if __name__ == '__main__':
    main()
