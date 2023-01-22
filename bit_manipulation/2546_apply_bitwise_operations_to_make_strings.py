class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        return ('1' in s) == ('1' in target)


solution = Solution()
res = solution.makeStringsEqual("00", "11")
print(res)
