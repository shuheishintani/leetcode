from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        max_avg = total / k
        for i in range(1, len(nums) - k + 1):
            total = total - nums[i - 1] + nums[i + k - 1]
            max_avg = max(max_avg, total / k)
        return max_avg


sol = Solution()
res = sol.findMaxAverage([1, 12, -5, -6, 50, 3], 4)
print(res)
