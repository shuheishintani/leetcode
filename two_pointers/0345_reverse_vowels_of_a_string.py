class Solution:
    # Stack
    def reverseVowels(self, s: str) -> str:
        vowels = []
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                vowels.append(s[i])

        res = ""
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                res += vowels.pop()
            else:
                res += s[i]
        return res

    # Two Pointers
    def reverseVowels2(self, s: str) -> str:
        vowels = set("AaEeIiOoUu")
        data = list(s)
        p1, p2 = 0, len(data) - 1
        while p1 < p2:
            if data[p1] in vowels and data[p2] in vowels:
                data[p1], data[p2] = data[p2], data[p1]
                p1 += 1
                p2 -= 1
            if data[p1] not in vowels:
                p1 += 1
            if data[p2] not in vowels:
                p2 -= 1
        return "".join(data)
