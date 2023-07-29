import heapq
from typing import List


class Solution:
    # Heap
    # Time complexity: O(K・logN)
    # Space complexity: O(K)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-v for v in nums]
        heapq.heapify(nums)
        res = 0
        for i in range(k):
            res = -heapq.heappop(nums)
        return res

    # Counting Sort
    # Time complexity: O(N+M)
    # Space complexity: O(M)
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        min_value = min(nums)
        max_value = max(nums)
        count = [0] * (max_value - min_value + 1)

        for num in nums:
            count[num - min_value] += 1

        remain = k
        for num in range(len(count) - 1, -1, -1):
            remain -= count[num]
            if remain <= 0:
                return num + min_value

        return -1
