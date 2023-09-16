class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        diff_x = abs(sx - fx)
        diff_y = abs(sy - fy)
        min_distance = min(diff_x, diff_y) + abs(diff_x - diff_y)
        return min_distance <= t if t != 1 else min_distance == 1
