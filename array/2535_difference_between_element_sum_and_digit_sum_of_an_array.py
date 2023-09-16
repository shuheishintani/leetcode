from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = 0
        digit_sum = 0

        for num in nums:
            element_sum += num
            for str_digit in str(num):
                digit_sum += int(str_digit)

        return abs(element_sum - digit_sum)
