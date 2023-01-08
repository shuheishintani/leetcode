import heapq
import math
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        res = 0
        nums = [-v for v in nums]
        heapq.heapify(nums)

        while k > 0:
            top = -1 * heapq.heappop(nums)
            res += top
            heapq.heappush(nums, -1 * math.ceil(top / 3))
            k -= 1

        return res
