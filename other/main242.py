class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if len(s) == 0:
            return True
        s_dic = {}
        t_dic = {}
        for i in range(len(s)):
            if s_dic.get(s[i]) is None:
                s_dic[s[i]] = 1
            else:
                s_dic[s[i]] += 1

            if t_dic.get(t[i]) is None:
                t_dic[t[i]] = 1
            else:
                t_dic[t[i]] += 1
        for k in s_dic.keys():
            vt = t_dic.get(k)
            if vt is None:
                return False
            if vt != s_dic[k]:
                return False
        return True


if __name__ == '__main__':
    ss = "anagram"
    tt = "nagaram"
    print(Solution().isAnagram(ss, tt))
