from typing import List


class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        row_seen_count, col_seen_count, total = 0, 0, 0
        row_seen, col_seen = [False] * n, [False] * n
        for qi in range(len(queries) - 1, -1, -1):
            op_type, index, val = queries[qi][0], queries[qi][1], queries[qi][2]
            if op_type == 0 and not row_seen[index]:
                row_seen_count += 1
                row_seen[index] = True
                total += (n - col_seen_count) * val
            if op_type == 1 and not col_seen[index]:
                col_seen_count += 1
                col_seen[index] = True
                total += (n - row_seen_count) * val
        return total
