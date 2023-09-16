from typing import List


class Solution:
    # using map
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                return True
            hashmap[num] = True
        return False

    # using set
    def containsDuplicate2(self, nums: List[int]) -> bool:
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
