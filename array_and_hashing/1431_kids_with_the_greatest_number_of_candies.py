from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_count = max(candies)
        res = [False] * len(candies)
        for i in range(len(candies)):
            res[i] = candies[i] + extraCandies >= max_count
        return res
