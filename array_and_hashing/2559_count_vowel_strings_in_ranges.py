from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def is_vowel(w: str) -> bool:
            vowels = ['a', 'i', 'u', 'e', 'o']
            return (len(w) == 1 and w[0] in vowels) or (w[0] in vowels and w[-1] in vowels)

        accum = [0]
        cur = 0
        for word in words:
            if word[0] in 'aiueo' and word[-1] in 'aiueo':
                cur += 1
            accum.append(cur)

        ans = []
        for [l, r] in queries:
            ans.append(accum[r + 1] - accum[l])
        return ans
