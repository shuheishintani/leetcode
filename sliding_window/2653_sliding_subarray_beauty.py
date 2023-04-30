from typing import List

from sortedcontainers import SortedList


class Solution:
    # TLE
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        for i in range(len(nums) - k + 1):
            left, right = i, i + k
            window = nums[left:right]
            v = min(sorted(window)[x - 1], 0)
            res.append(v)
        return res

    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        vals = SortedList()
        for i, v in enumerate(nums):
            vals.add(v)
            if i >= k: vals.remove(nums[i - k])
            if i >= k - 1: res.append(min(0, vals[x - 1]))
        return res


solution = Solution()
res = solution.getSubarrayBeauty([1, -1, -3, -2, 3], 3, 2)
print(res)
