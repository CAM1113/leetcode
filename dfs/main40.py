# 40. 组合总和 II
# 给定一个数组candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。
#
# candidates中的每个数字在每个组合中只能使用一次。
#
# 说明：
#
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/combination-sum-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        list.sort(candidates)
        result = []
        chosen = []
        self.find_target(candidates, target, chosen, result)
        return result

    def find_target(self, candicates_, target, chosen, result):
        al = sum(chosen)
        for i in range(len(candicates_)):
            if al + candicates_[i] == target:
                cho = chosen.copy()
                cho.append(candicates_[i])
                if cho not in result:
                    result.append(cho)
            elif al + candicates_[i] < target and i + 1 < len(candicates_):
                chosen.append(candicates_[i])
                self.find_target(candicates_[i + 1:len(candicates_)], target, chosen, result)
                chosen.pop()
            else:
                break


if __name__ == '__main__':
    cand = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    result = Solution().combinationSum2(cand, target)
    print(result)
