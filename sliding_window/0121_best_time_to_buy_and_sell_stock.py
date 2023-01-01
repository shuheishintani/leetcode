from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = float('inf')
        cur_max_profit = 0
        for price in prices:
            if price < cur_min:
                cur_min = price
            if price - cur_min > cur_max_profit:
                cur_max_profit = price - cur_min
        return int(cur_max_profit)


solution = Solution()
ans = solution.maxProfit([7, 1, 5, 3, 6, 4])
print(ans)
