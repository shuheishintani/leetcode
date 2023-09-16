from collections import defaultdict
from typing import List


class Solution:
    # categorize by sorted string
    # - time: O(MNlogN)
    # - space: O(MN)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in hashmap:
                hashmap[sorted_word].append(word)
            else:
                hashmap[sorted_word] = [word]

        res = []
        for anagrams in hashmap.values():
            res.append(anagrams)

        return res

    # categorize by count
    # - time: O(MN)
    # - space: O(MN)
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)

        return list(res.values())
