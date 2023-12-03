class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        min_length = min(len(s1), len(s2), len(s3))
        same_length = 0
        for i in range(min_length):
            if s1[i] == s2[i] == s3[i]:
                same_length += 1
            else:
                break
        return -1 if same_length == 0 else len(s1) + len(s2) + len(s3) - same_length * 3


sol = Solution()
print(sol.findMinimumOperations('dac', 'bac', 'cac'))
