from collections import Counter


class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        keys1 = list(freq1.keys())
        keys2 = list(freq2.keys())

        for c1 in keys1:
            for c2 in keys2:
                freq1[c1] -= 1
                freq1[c2] += 1
                freq2[c1] += 1
                freq2[c2] -= 1

                if freq1[c1] == 0:
                    del freq1[c1]
                if freq2[c2] == 0:
                    del freq2[c2]

                if len(freq1) == len(freq2):
                    return True

                freq1[c1] += 1
                freq1[c2] -= 1
                freq2[c1] -= 1
                freq2[c2] += 1

                if freq1[c2] == 0:
                    del freq1[c2]
                if freq2[c1] == 0:
                    del freq2[c1]

        return False
