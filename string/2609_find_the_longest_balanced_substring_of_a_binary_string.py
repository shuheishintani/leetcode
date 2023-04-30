class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        res, tmp = 0, "01"
        while len(tmp) <= len(s):
            if tmp in s:
                res = len(tmp)
            tmp = '0' + tmp + '1'
        return res
