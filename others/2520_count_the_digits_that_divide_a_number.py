class Solution:
    def countDigits(self, num: int) -> int:
        res = 0
        for c in str(num):
            if num % int(c) == 0:
                res += 1
        return res
