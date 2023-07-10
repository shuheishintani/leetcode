class Solution:
    # DP
    # - time: O(N)
    # - space: O(1)
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        two_step_before = 1
        one_step_before = 2
        res = 0

        for i in range(3, n + 1):
            res = two_step_before + one_step_before
            two_step_before = one_step_before
            one_step_before = res

        return res

    # DP (clearner way)
    def climbStairs2(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            tmp = one
            one = one + two
            two = tmp

        return one


solution = Solution()
ans = solution.climbStairs(4)
print(ans)
