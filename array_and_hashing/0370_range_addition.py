from typing import List


class Solution:
    # sweep line
    # - time: O(N+M)
    # - space: O(1)
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0] * length

        for start, end, value in updates:
            res[start] += value
            if end + 1 < length:
                res[end + 1] -= value

        for i in range(1, length):
            res[i] += res[i - 1]

        return res
