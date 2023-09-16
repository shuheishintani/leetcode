from typing import List


class Solution:
    # TLE
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        for k, n in enumerate(arr):
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if mat[i][j] == n:
                        mat[i][j] = 0
                        row_sum = sum(mat[i])
                        col_sum = 0
                        for i2 in range(len(mat)):
                            col_sum += mat[i2][j]
                        if row_sum == 0 or col_sum == 0:
                            return k

    # using hash map
    def firstCompleteIndex2(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        hash_map = {}
        for i in range(m):
            for j in range(n):
                hash_map[mat[i][j]] = [i, j]

        row = [0] * m
        col = [0] * n
        for i in range(len(arr)):
            x = hash_map[arr[i]]
            row[x[0]] += 1
            col[x[1]] += 1
            if row[x[0]] == n or col[x[1]] == m:
                return i

        return -1


sol = Solution()
res = sol.firstCompleteIndex([2, 8, 7, 4, 1, 3, 5, 6, 9], [[3, 2, 5], [1, 4, 6], [8, 7, 9]])
print(res)
