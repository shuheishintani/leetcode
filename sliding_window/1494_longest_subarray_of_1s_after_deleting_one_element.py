from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = zeros = ans = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            ans = max(ans, right - left + 1 - zeros)

        return ans - 1 if ans == len(nums) else ans


sol = Solution()
res = sol.longestSubarray([1, 1, 0, 1])
print(res)
