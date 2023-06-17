from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        distinct_nums1 = []
        for num in nums1:
            if num not in set2:
                distinct_nums1.append(num)
                set2.add(num)

        distinct_nums2 = []
        for num in nums2:
            if num not in set1:
                distinct_nums2.append(num)
                set1.add(num)

        return [distinct_nums1, distinct_nums2]
