class Solution:
    def monkeyMove(self, n: int) -> int:
        mod = 10 ** 9 + 7
        return (pow(2, n, mod) - 2) % (10 ** 9 + 7)


solution = Solution()
res = solution.monkeyMove(4)
print(res)
