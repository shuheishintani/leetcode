from typing import List


class Solution:
    # naive approach (TLE)
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        res = [0] * len(word)
        cur = ""
        for i, c in enumerate(word):
            cur += c
            if int(cur) % m == 0:
                res[i] = 1
                cur = ""
        return res

    # faster solution
    def divisibilityArray2(self, word: str, m: int) -> List[int]:
        ans = []
        mod = 0
        for c in word:
            mod = (mod * 10 + int(c)) % m
            ans.append(1 if mod % m == 0 else 0)
        return ans


solution = Solution()
res = solution.divisibilityArray("998244353", 3)
print(res)
