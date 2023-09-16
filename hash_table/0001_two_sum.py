from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for i, num in enumerate(nums):
            if num in comp:
                return [i, comp[num]]
            comp[target - num] = i
