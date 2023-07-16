from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        for j in range(len(nums)):
            if nums[j] - nums[i] > k * 2:
                i += 1
        return j - i + 1
