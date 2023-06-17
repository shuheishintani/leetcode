from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            return n == 0 or (n == 1 and flowerbed[0] == 0)

        serial_empty_count = 1
        for i, flower in enumerate(flowerbed):
            if flower == 0:
                serial_empty_count += 1
            else:
                serial_empty_count = 0

            if serial_empty_count == 3 or (serial_empty_count == 2 and i == len(flowerbed) - 1):
                n -= 1
                serial_empty_count = 1

            if n == 0:
                return True

        return False

    # Refactored
    def canPlaceFlowers2(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                empty_left = i == 0 or flowerbed[i - 1] == 0
                empty_right = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0
                if empty_left and empty_right:
                    flowerbed[i] = 1
                    count += 1
        return count >= n
