import math
from typing import List


class Solution:
    # my answer (TLE)
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        counter = {}
        prime_list = self.getPrimeList(max(nums))
        index = 0
        remain = 1
        for n in nums:
            remain *= n

        while index < len(prime_list):
            if remain % prime_list[index] == 0:
                counter[prime_list[index]] = counter.get(prime_list[index], 0) + 1
                remain //= prime_list[index]
            else:
                index += 1

        if remain != 1:
            counter[remain] = counter.get(remain, 0) + 1

        return len(counter)

    def getPrimeList(self, n: int) -> List[int]:
        prime_table = [True] * (n + 1)
        prime_table[0], prime_table[1] = False, False
        for i in range(2, n + 1):
            if not prime_table[i]:
                continue

            q = i * 2
            while q <= n:
                prime_table[q] = False
                q += i

        res = []
        for i, is_prime in enumerate(prime_table):
            if is_prime:
                res.append(i)
        return res

    # voted answer
    # - time: O(N * sqrt(N))
    # - space: O(N)
    def distinctPrimeFactors2(self, nums: List[int]) -> int:
        prime_factors = set()

        for num in nums:
            current_prime_factors = self.getPrimeFactors(num)
            prime_factors.update(current_prime_factors)

        return len(prime_factors)

    def getPrimeFactors(self, num: int) -> set:
        prime_factors = set()

        while num % 2 == 0:
            prime_factors.add(2)
            num /= 2

        for i in range(3, int(math.sqrt(num)) + 1, 2):
            while num % i == 0:
                prime_factors.add(i)
                num /= i

        if num > 2:
            prime_factors.add(num)

        return prime_factors
