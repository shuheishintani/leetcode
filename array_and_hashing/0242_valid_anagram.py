class Solution:
    # using counter
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = {}
        for c in s:
            if c not in counter:
                counter[c] = 0
            counter[c] += 1

        for c in t:
            if c in counter:
                counter[c] -= 1
                if counter[c] == 0:
                    del counter[c]
            else:
                return False
        return True

    # using counter (simpler way)
    def isAnagram2(self, s: str, t: str) -> bool:
        count_s, count_t = {}, {}
        for c in s:
            count_s[c] = count_s.get(c, 0) + 1
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        return count_s == count_t
