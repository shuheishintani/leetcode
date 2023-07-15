from functools import cache
from typing import List


class Solution:
    # Bottom-Up
    # - time: O(N)
    # - space: O(N)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            one_step = min_cost[i - 1] + cost[i - 1]
            two_step = min_cost[i - 2] + cost[i - 2]
            min_cost[i] = min(one_step, two_step)

        return min_cost[-1]

    # Top-Down
    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        def minimum_cost(i):
            if i <= 1:
                return 0

            if i in memo:
                return memo[i]

            down_one = cost[i - 1] + minimum_cost(i - 1)
            down_two = cost[i - 2] + minimum_cost(i - 2)
            memo[i] = min(down_one, down_two)
            return memo[i]

        memo = {}
        return minimum_cost(len(cost))

    # Top-Down (using @cache)

    def minCostClimbingStairs3(self, cost: List[int]) -> int:
        @cache
        def minimum_cost(i):
            if i <= 1:
                return 0

            down_one = cost[i - 1] + minimum_cost(i - 1)
            down_two = cost[i - 2] + minimum_cost(i - 2)
            return min(down_one, down_two)

        return minimum_cost(len(cost))
