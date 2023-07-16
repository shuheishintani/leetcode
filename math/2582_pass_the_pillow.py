class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        res = 1
        count_up = True
        for i in range(time):
            if res >= n:
                count_up = False
            elif res == 1:
                count_up = True

            if count_up:
                res += 1
            else:
                res -= 1

        return res

    # simpler way
    def passThePillow2(self, n: int, time: int) -> int:
        rounds = time // (n - 1)
        k = time % (n - 1)
        return k + 1 if rounds % 2 == 0 else n - k


solution = Solution()
res = solution.passThePillow(18, 38)
print(res)
