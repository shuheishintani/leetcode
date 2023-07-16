from collections import Counter
from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        counter = Counter(nums)
        [target, total_count] = counter.most_common(1)[0]

        left_count = 0
        for i, n in enumerate(nums):
            if n == target:
                left_count += 1
                if left_count * 2 > i + 1:
                    break

        return i if (total_count - left_count) * 2 > len(nums) - 1 - i else -1


sol = Solution()
res = sol.minimumIndex([3, 3, 3, 3, 7, 2, 2])
print(res)
