class Solution:
    # shrink array
    def isSubsequence(self, s: str, t: str) -> bool:
        for c1 in s:
            found = False
            for j, c2 in enumerate(t):
                if c1 == c2:
                    t = t[j + 1:]
                    found = True
                    break
            if not found:
                return False
        return True

    # two pointers
    def isSubsequence2(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


solution = Solution()
res = solution.isSubsequence("abc", "ahbgdc")
print(res)
