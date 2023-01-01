import heapq
from typing import List


class Solution:
    # using heapq
    # - time: O(NlogN)
    # - space: O(N)
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-v for v in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            top = -1 * heapq.heappop(stones)
            sub_top = -1 * heapq.heappop(stones)
            if top > sub_top:
                heapq.heappush(stones, sub_top - top)

        return -1 * heapq.heappop(stones) if len(stones) > 0 else 0


solution = Solution()
res = solution.lastStoneWeight([2, 7, 4, 1, 8, 1])
print(res)
