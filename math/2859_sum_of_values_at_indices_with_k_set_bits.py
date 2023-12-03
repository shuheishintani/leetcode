from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        res = 0
        for i, n in enumerate(nums):
            if bin(i).count('1') == k:
                res += n
        return res
