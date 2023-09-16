from typing import List


class Solution:
    # sort
    def replaceElements(self, arr: List[int]) -> List[int]:
        cur_max = -1
        rev = list(reversed(arr))
        for i, num in enumerate(rev):
            rev[i] = cur_max
            cur_max = max(cur_max, num)
        return list(reversed(rev))

    # without sort
    def replaceElements2(self, arr: List[int]) -> List[int]:
        right_max = -1
        for i in range(len(arr) - 1, -1, -1):
            new_max = max(right_max, arr[i])
            arr[i] = right_max
            right_max = new_max
        return arr
