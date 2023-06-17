from typing import List


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1
        nums.sort()
        return nums[1]

    # O(1) solution
    def findNonMinOrMax2(self, nums: List[int]) -> int:
        return -1 if len(nums) < 3 else sum(nums[:3]) - min(nums[:3]) - max(nums[:3])


sol = Solution()
res = sol.findNonMinOrMax([3, 2, 1, 4])
print(res)
