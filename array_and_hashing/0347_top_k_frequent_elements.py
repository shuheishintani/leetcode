import heapq
from collections import defaultdict, Counter
from typing import List


class Solution:
    # using heap
    # - time: O(Nlogk)
    # - space: O(N+k)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)

    # bucket sort
    # - time: O(N)
    # - space: O(N)
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        freq = [[] for i in range(len(nums) + 1)]

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
