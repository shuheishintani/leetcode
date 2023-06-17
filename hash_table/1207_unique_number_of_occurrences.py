from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        count_set = set()
        for count in counter.values():
            if count in count_set:
                return False
            count_set.add(count)
        return True
