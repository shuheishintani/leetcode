from typing import List


class Solution:
    # brute force (TLE)
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        sums = []
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                sums.append(nums[i] + nums[j])

        res = 0
        for s in sums:
            if lower <= s <= upper:
                res += 1

        return res

    # two pointers
    # - time: O(N)
    # - space: O(1)
    def countFairPairs2(self, nums: List[int], lower: int, upper: int) -> int:
        def countLess(val: int) -> int:
            res, j = 0, len(nums) - 1
            for i in range(len(nums)):
                while i < j and nums[i] + nums[j] > val:
                    j -= 1
                res += max(0, j - i)
            return res

        nums.sort()
        return countLess(upper) - countLess(lower - 1)


solution = Solution()
res = solution.countFairPairs2([0, 1, 7, 4, 4, 5], 3, 6)
print(res)
