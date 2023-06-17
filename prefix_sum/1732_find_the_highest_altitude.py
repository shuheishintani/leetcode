from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0]
        for g in gain:
            res.append(res[len(res) - 1] + g)
        return max(res)
