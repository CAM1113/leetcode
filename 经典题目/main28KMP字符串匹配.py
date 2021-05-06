def getPMT(needle: str):
    PMT = [0 for _ in range(len(needle))]
    PMT[0] = -1
    i = 0
    j = -1
    while i < len(needle)-1:
        if j == -1 or needle[i] == needle[j]:
            i += 1
            j += 1
            PMT[i] = j
        else:
            j = PMT[j]
    return PMT


# KMP算法做字符串匹配
class Solution:
    def strStr(self, haystack: str, needle: str):
        if len(needle) == 0:
            return 0
        PMT = getPMT(needle)
        index_t = 0
        index_m = 0
        t_len = len(haystack)
        m_len = len(needle)
        while index_t < t_len and index_m < m_len:
            if haystack[index_t] == needle[index_m]:
                index_t += 1
                index_m += 1
            else:
                if index_m == 0:
                    index_t += 1
                else:
                    index_m = PMT[index_m]
        if index_m == m_len:
            return index_t - index_m
        return -1