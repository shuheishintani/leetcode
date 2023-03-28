class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        res = 0
        for i in range(k):
            if numOnes > 0:
                res += 1
                numOnes -= 1
            elif numZeros > 0:
                numZeros -= 1
            elif numNegOnes > 0:
                res -= 1
                numNegOnes -= 1
        return res

    # one-liner
    def kItemsWithMaximumSum2(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        return min(k, numOnes) - max(0, k - numOnes - numZeros)


solution = Solution()
res = solution.kItemsWithMaximumSum(3, 2, 0, 2)
print(res)
