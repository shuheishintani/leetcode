from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        hash_set = set()
        for [start, end] in nums:
            for i in range(start, end + 1):
                hash_set.add(i)
        return len(hash_set)
