from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        res = 0
        while len(nums) > 1:
            res += int(str(nums[0]) + str(nums[-1]))
            nums = nums[1:-1]

        if len(nums) > 0:
            res += nums[0]

        return res

