class Solution:
    # TLE
    def countOdds(self, low: int, high: int) -> int:
        res = 0
        for i in range(low, high + 1):
            if i % 2 != 0:
                res += 1
        return res

    def countOdds2(self, low: int, high: int) -> int:
        odd = (high - low) // 2
        if low % 2 == 1 or high % 2 == 1:
            odd += 1
        return odd
