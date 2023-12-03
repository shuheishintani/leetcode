class Solution:
    def minimumSteps(self, s: str) -> int:
        reversed_s = s[::-1]
        res, zero_count = 0, 0
        for i in range(len(reversed_s)):
            if reversed_s[i] == '1':
                res += zero_count
            else:
                zero_count += 1
        return res


sol = Solution()
print(sol.minimumSteps("1001001"))
