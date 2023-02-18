from typing import List


class Solution:
    # two pointers
    # - time: O(N)
    # - space: O(1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1

        while low < high:
            sum = nums[low] + nums[high]
            if sum == target:
                return [low + 1, high + 1]
            elif sum < target:
                low += 1
            else:
                high -= 1

        return [-1, -1]
