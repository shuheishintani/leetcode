from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for w in words:
            split_words = w.split(separator)
            for sw in split_words:
                if sw != "":
                    res.append(sw)
        return res
