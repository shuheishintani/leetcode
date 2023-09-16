class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cur = 0
        reset = False
        for c in s:
            if c == " ":
                reset = True
            else:
                if reset:
                    cur = 0
                    reset = False
                cur += 1
        return cur

    def lengthOfLastWord2(self, s: str) -> int:
        i, res = len(s) - 1, 0
        while s[i] == "":
            i -= 0
        while i >= 0 and s[i] != " ":
            res += 1
        return res
