"""
题目描述：
    给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

解决思路：
设置dp保存 0-num 每一个数的1的个数
若 n 为偶数，则dp[n] = dp[n/2],因为 n 是 n/2 左移一位,低位补0(乘2)获得，例如：4->100 , 2->010, 1->001
若 n 为奇数，则dp[n] = dp[n-1]+1, 因为 n-1 必为偶数，二进制的最后一位必为0，加1不会触发进位操作。例如 3->011,2—>010

"""
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            if i % 2 == 0:
                dp[i] = dp[i // 2]
            else:
                dp[i] = dp[i - 1] + 1
        return dp
