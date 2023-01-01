from typing import List


class Solution:
    # greedy
    # - time: O(N)
    # - space: O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        current_subarray = max_subarray = nums[0]

        for num in nums[1:]:
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)

        return max_subarray


solution = Solution()
res = solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(res)
