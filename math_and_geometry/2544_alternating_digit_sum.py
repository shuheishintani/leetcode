class Solution:
    def alternateDigitSum(self, n: int) -> int:
        res = 0
        for i, str_digit in enumerate(str(n)):
            if i % 2 == 0:
                res += int(str_digit)
            else:
                res -= int(str_digit)
        return res


solution = Solution()
res = solution.alternateDigitSum(886996)
print(res)
