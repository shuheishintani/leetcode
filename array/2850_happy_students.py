from typing import List


class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(-1, len(nums)):
            left_met = nums[i] > 0 if i == -1 else i + 1 > nums[i]
            right_met = (i == len(nums) - 1) or i + 1 < nums[i + 1]
            if left_met and right_met:
                res += 1
        return res

    def countWays2(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(1, len(nums) - 1):
            if nums[i - 1] < i < nums[i]:
                res += 1
        if min(nums) > 0:
            res += 1
        if max(nums) < len(nums):
            res += 1
        return res


sol = Solution()
res = sol.countWays([6, 0, 3, 3, 6, 7, 2, 7])
print(res)
