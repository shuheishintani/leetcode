from typing import List


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        min_i, max_i = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                min_i = i
            if nums[i] == len(nums):
                max_i = i

        if max_i > min_i:
            return min_i + len(nums) - 1 - max_i
        else:
            return min_i + len(nums) - 1 - max_i - 1
