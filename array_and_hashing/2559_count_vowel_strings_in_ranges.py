from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        accum = [0]
        cur = 0
        for word in words:
            if word[0] in 'aiueo' and word[-1] in 'aiueo':
                cur += 1
            accum.append(cur)

        ans = []
        for [l, r] in queries:
            ans.append(accum[r + 1] - accum[l])
        return ans
