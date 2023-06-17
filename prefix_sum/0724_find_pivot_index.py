from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix_sum = 0
        for i in range(0, len(nums)):
            if prefix_sum * 2 + nums[i] == total:
                return i
            prefix_sum += nums[i]
        return -1
