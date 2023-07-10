from typing import List


class Solution:
    # DP
    # - time: O(N)
    # - space: O(N)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            one_step = min_cost[i - 1] + cost[i - 1]
            two_step = min_cost[i - 2] + cost[i - 2]
            min_cost[i] = min(one_step, two_step)

        return min_cost[-1]
