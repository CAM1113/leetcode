from typing import List
# 桶排序的思想

def get_id(n, t):
    if n >= 0:
        return int(n / (t + 1))
    else:
        return int((n + 1) / (t + 1) - 1)


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        bucket = {}
        for index, n in enumerate(nums):
            bucket_order = get_id(n, t)
            if bucket_order in bucket.keys():
                return True
            if bucket_order + 1 in bucket.keys() and abs(bucket[bucket_order + 1] - n) <= t:
                return True
            if bucket_order - 1 in bucket.keys() and abs(bucket[bucket_order - 1] - n) <= t:
                return True
            bucket[bucket_order] = n
            if index - k >= 0:
                remove_bucket_order = get_id(nums[index-k], t)
                bucket.pop(remove_bucket_order)
        return False


if __name__ == '__main__':
    nums = [1,5,9,1,5,9]
    k = 2
    t = 3
    print(Solution().containsNearbyAlmostDuplicate(nums, k, t))
