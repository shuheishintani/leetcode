from typing import List


class Solution:
    # brute force (TLE)
    # - time: O(N^2M)
    # - space: O(1)
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        res = [[0 for j in range(n)] for i in range(n)]
        for query in queries:
            row1 = query[0]
            col1 = query[1]
            row2 = query[2]
            col2 = query[3]

            for i in range(row1, row2 + 1):
                for j in range(col1, col2 + 1):
                    res[i][j] += 1

        return res

    # sweep line
    # - time: O(N^2+M)
    # - space: O(1)
    def rangeAddQueries2(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        for r1, c1, r2, c2 in queries:
            for r in range(r1, r2 + 1):
                res[r][c1] += 1
                if c2 + 1 < n:
                    res[r][c2 + 1] -= 1
        for r in range(n):
            for c in range(1, n):
                res[r][c] += res[r][c - 1]
        return res
