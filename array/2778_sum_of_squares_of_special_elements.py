from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        res = 0
        for i, n in enumerate(nums):
            if len(nums) % (i + 1) == 0:
                res += n * n
        return res
