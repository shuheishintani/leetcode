from typing import List


class Solution:
    # using hash set
    # - time: O(N)
    # - space: O(N)
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in num_set:
                consecutive = 1
                cur = num + 1
                while cur in num_set:
                    consecutive += 1
                    cur += 1
                if consecutive > res:
                    res = consecutive
        return res

    # using hash set (cleaner way)
    def longestConsecutive2(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in num_set:
                length = 1
                while n + length in num_set:
                    length += 1
                longest = max(length, longest)
        return longest
