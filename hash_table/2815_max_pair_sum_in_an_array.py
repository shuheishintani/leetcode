from collections import defaultdict
from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        res = -1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                n1_max = 0
                n2_max = 0
                for c1 in str(nums[i]):
                    if int(c1) > n1_max:
                        n1_max = int(c1)
                for c2 in str(nums[j]):
                    if int(c2) > n2_max:
                        n2_max = int(c2)
                if n1_max == n2_max:
                    res = max(res, nums[i] + nums[j])
        return res

    def maxSum2(self, nums: List[int]) -> int:
        ans = -1
        d = defaultdict(list)

        for num in nums:
            d[max(str(num))].append(num)

        for c in d:
            if len(d[c]) < 2:
                continue
            ans = max(ans, sum(sorted(d[c])[-2:]))

        return ans


sol = Solution()
res = sol.maxSum([51, 71, 17, 24, 42])
print(res)
