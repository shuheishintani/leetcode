from collections import defaultdict
from typing import List


class Solution:
    # Two pointers
    def maxOperations(self, nums: List[int], k: int) -> int:
        res = 0
        left, right = 0, len(nums) - 1
        nums.sort()
        while left < right:
            if nums[left] + nums[right] > k:
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                res += 1
                left += 1
                right -= 1
        return res

    # Counter
    def maxOperations2(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        res = 0
        for num in nums:
            comp = k - num
            if counter[comp] > 0:
                counter[comp] -= 1
                res += 1
            else:
                counter[num] += 1
        return res
