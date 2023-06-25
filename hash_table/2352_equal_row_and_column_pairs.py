from collections import Counter
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = []
        for row in grid:
            rows.append(tuple(row))
        row_counter = Counter(rows)

        cols = []
        for i in range(len(grid)):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            cols.append(tuple(col))
        col_counter = Counter(cols)

        res = 0
        for row_key in row_counter.keys():
            res += row_counter[row_key] * col_counter[row_key]
        return res


sol = Solution()
res = sol.equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]])
