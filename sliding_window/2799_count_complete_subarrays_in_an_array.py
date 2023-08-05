from collections import Counter
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        distinct_elements = len(set(nums))
        count, left, right = 0, 0, 0
        counter = Counter()

        while right < n:
            counter[nums[right]] += 1
            while len(counter) == distinct_elements:
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1
                count += n - right
            right += 1

        return count


sol = Solution()
res = sol.countCompleteSubarrays([1, 2, 1, 2, 2])
# print(res)
