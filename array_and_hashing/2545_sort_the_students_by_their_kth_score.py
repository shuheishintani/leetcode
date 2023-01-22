import heapq
from typing import List


class Solution:
    # using heap and hashmap
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        col = []
        heapq.heapify(col)
        row_map = {}
        for row in score:
            col.append(row[k])
            heapq.heappush(col, -row[k])
            row_map[row[k]] = row

        res = []
        for i in range(len(score)):
            top = -heapq.heappop(col)
            res.append(row_map[top])
        return res

    # sort
    def sortTheStudents2(self, score: List[List[int]], k: int) -> List[List[int]]:
        return sorted(score, key=lambda a: -a[k])


solution = Solution()
res = solution.sortTheStudents([[3, 4], [5, 6]], 0)
print(res)
