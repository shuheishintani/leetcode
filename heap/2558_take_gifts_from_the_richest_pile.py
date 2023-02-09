import math
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            gifts = sorted(gifts, reverse=True)
            gifts[0] = math.floor(math.sqrt(gifts[0]))
        return sum(gifts)
