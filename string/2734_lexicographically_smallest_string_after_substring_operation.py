class Solution:
    def smallestString(self, s: str) -> str:
        i = 0
        s = list(s)
        while i < len(s) and s[i] == 'a':
            i += 1
        if i == len(s):
            s[-1] = 'z'
        while i < len(s) and s[i] != 'a':
            s[i] = chr(ord(s[i]) - 1)
            i += 1
        return ''.join(s)
