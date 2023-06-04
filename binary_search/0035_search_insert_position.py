from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            pivot = (l + r) // 2
            if nums[pivot] == target:
                return pivot
            elif target < nums[pivot]:
                r = pivot - 1
            else:
                l = pivot + 1
        return l
