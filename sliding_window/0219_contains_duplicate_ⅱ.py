from collections import defaultdict
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counter = defaultdict(int)
        for i in range(k):
            if i == len(nums):
                break

            if counter[nums[i]] > 0:
                return True
            else:
                counter[nums[i]] += 1

        print(len(nums) - k)

        for i in range(1, len(nums) - k + 1):
            if counter[nums[i + k - 1]] > 0:
                return True
            else:
                counter[nums[i - 1]] -= 1
                counter[nums[i + k - 1]] += 1

        return False

    # simplified
    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False
