# LCP 18. 早餐组合

# 小扣在秋日市集选择了一家早餐摊位，一维整型数组 staple 中记录了每种主食的价格，一维整型数组 drinks 中记录了每种饮料的价格。小扣的计划选择一份主食和一款饮料，且花费不超过 x 元。请返回小扣共有多少种购买方案。
#
# 注意：答案需要以 1e9 + 7 (1000000007) 为底取模，如：计算初始结果为：1000000008，请返回 1
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/2vYnGI
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


def count_drinks_mid(drinks, target, start, end):
    if end - start <= 3:
        i = start
        while i <= end:
            if drinks[i] > target:
                break
            i += 1
        i -= 1
        if i == -1:
            return 0
        else:
            return i + 1
    middle = (end + start) // 2
    if drinks[middle] <= target:
        return count_drinks_mid(drinks, target, middle, end)
    else:
        return count_drinks_mid(drinks, target, start, middle)


def count_drinks_back(drinks, target, end):
    while drinks[end] > target and end >= 0:
        end -= 1
    return end


class Solution:
    def breakfastNumber(self, staple, drinks, x):
        list.sort(staple)
        list.sort(drinks)
        staple_i = 0
        count = 0
        end = len(drinks) - 1
        while staple_i < len(staple):
            if staple[staple_i] > x:
                break
            target = x - staple[staple_i]
            # count += count_drinks_mid(drinks, target, 0, len(drinks) - 1)
            end = count_drinks_back(drinks, target, end)
            count += (end + 1)
            if end < 0:
                break
            staple_i += 1
        return count % (1000000007)


if __name__ == '__main__':
    s = [7, 3, 4, 3, 9, 9, 10, 8, 8, 3]

    d = [7, 10, 6, 7, 5, 2, 8, 4, 5, 8]

    t = 5
    print(Solution().breakfastNumber(s, d, t))
