from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]

    # Space optimal
    def rob2(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max_profit_prev = nums[0]
        max_profit = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            cur = max(max_profit_prev + nums[i], max_profit)
            max_profit_prev = max_profit
            max_profit = cur

        return max_profit
