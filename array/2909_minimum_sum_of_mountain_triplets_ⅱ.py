import sys
from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        prefix_min = []
        cur_min = sys.maxsize
        for n in nums:
            if n < cur_min:
                cur_min = n
            prefix_min.append(cur_min)

        suffix_min = []
        cur_min = sys.maxsize
        for n in nums[::-1]:
            if n < cur_min:
                cur_min = n
            suffix_min.append(cur_min)
        suffix_min.reverse()

        min_mountain = sys.maxsize
        for i in range(1, len(nums) - 1):
            if prefix_min[i - 1] < nums[i] and suffix_min[i + 1] < nums[i]:
                mountain = prefix_min[i - 1] + nums[i] + suffix_min[i + 1]
                if mountain < min_mountain:
                    min_mountain = mountain

        if min_mountain == sys.maxsize:
            return -1

        return min_mountain
