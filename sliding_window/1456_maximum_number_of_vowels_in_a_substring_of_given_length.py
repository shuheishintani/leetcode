class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        left, right = 0, min(k, len(s))
        initial_window = s[left:right]
        count, res = 0, 0
        for c in initial_window:
            if c in vowels:
                count += 1
                res += 1

        while right < len(s):
            print(s[left:right], count)
            left += 1
            right += 1
            if s[left - 1] in vowels:
                count -= 1
            if s[right - 1] in vowels:
                count += 1
            res = max(res, count)

        return res


sol = Solution()
res = sol.maxVowels("abciiidef", 3)
print(res)
