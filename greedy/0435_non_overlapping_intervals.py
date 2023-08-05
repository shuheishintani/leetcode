from typing import List


class Solution:
    # Sort by start time
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev, i, ans = 0, 1, 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[prev][1]:
                ans += 1
                if intervals[i][1] < intervals[prev][1]:
                    prev = i
            else:
                prev = i
        return ans

    # Sort by end time
    def eraseOverlapIntervals2(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0
        k = float('-inf')
        for x, y in intervals:
            if x >= k:
                k = y
            else:
                ans += 1
        return ans
