class Solution:
    # using hash set
    # - time: O(logN)
    # - space: O(logN)
    def isHappy(self, n: int) -> bool:
        cur = n
        visit = set()
        is_happy = False
        while not is_happy:
            square_sum = 0
            for c in str(cur):
                square_sum += int(c) ** 2
            if square_sum in visit:
                return False
            elif square_sum == 1:
                is_happy = True
            else:
                cur = square_sum
                visit.add(square_sum)
        return is_happy

    # using hash set (cleaner way)
    def isHappy2(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sum_of_squares(n)

            if n == 1:
                return True

        return False

    # cycle finding algorithm
    # - time: O(logN)
    # - space: O(1)
    def isHappy3(self, n: int) -> bool:
        slow_runner = n
        fast_runner = self.sum_of_squares(n)

        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = self.sum_of_squares(slow_runner)
            fast_runner = self.sum_of_squares(self.sum_of_squares(fast_runner))

        return fast_runner == 1

    def sum_of_squares(self, n: int) -> int:
        output = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output


solution = Solution()
res = solution.isHappy(2)
print(res)
