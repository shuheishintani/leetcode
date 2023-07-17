from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            binary = format(i, "b")
            count = 0
            for c in binary:
                if c == "1":
                    count += 1
            ans.append(count)
        return ans

    # Pop Count
    # Time complexity: O(NlogN)
    # Space complexity: O(1)
    def countBits2(self, n: int) -> List[int]:
        def pop_count(x: int) -> int:
            count = 0
            while x != 0:
                x &= x - 1
                count += 1
            return count

        ans = [0] * (n + 1)
        for x in range(n + 1):
            ans[x] = pop_count(x)
        return ans

    # DP + Last Significant Bit
    # Time complexity: O(N)
    # Space complexity: O(1)
    def countBits3(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            ans[x] = ans[x >> 1] + (x & 1)
        return ans
