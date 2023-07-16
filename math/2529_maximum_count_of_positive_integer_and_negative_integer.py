from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        positive_count = 0
        negative_count = 0
        for n in nums:
            if n > 0:
                positive_count += 1
            if n < 0:
                negative_count += 1
        return max(positive_count, negative_count)
