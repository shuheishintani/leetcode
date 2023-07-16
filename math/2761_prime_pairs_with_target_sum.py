from math import sqrt
from typing import List


class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        def getPrimes(n: int) -> List[int]:
            if n <= 2:
                return []

            numbers = [False, False] + [True] * (n - 2)
            for p in range(2, int(sqrt(n)) + 1):
                if numbers[p]:
                    for multiple in range(p * p, n, p):
                        numbers[multiple] = False

            res = []
            for i, is_prime in enumerate(numbers):
                if is_prime:
                    res.append(i)

            return res

        primes = getPrimes(n)
        comp = {}
        for prime in primes:
            comp[n - prime] = True

        res = []
        for prime in primes:
            if prime in comp:
                res.append([prime, n - prime])
                comp.pop(n - prime)

        return res
