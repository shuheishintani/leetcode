class Solution:
    # greedy
    # - time: O(N)
    # - space: O(1)
    def minimumPartition(self, s: str, k: int) -> int:
        ans, cur = 1, 0
        for d in s:
            if int(d) > k:
                return -1
            cur = 10 * cur + int(d)
            if cur > k:
                ans += 1
                cur = int(d)
        return ans
