# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 2
        while index < len(nums):
            print(len(nums))
            if nums[index] == nums[index - 2]:
                del nums[index]
            else:
                index += 1
        return len(nums)


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    s = Solution()
    len = s.removeDuplicates(nums)
    print(len)
    print(nums)
