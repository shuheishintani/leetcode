from typing import List


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        def get_left_sum(nums: List[int]) -> List[int]:
            left_sum = []
            cur = 0
            for i in range(len(nums)):
                if i == 0:
                    left_sum.append(0)
                    continue
                left_sum.append(cur + nums[i - 1])
                cur = left_sum[i]
            return left_sum

        left_sum = get_left_sum(nums)
        nums.reverse()
        right_sum = get_left_sum(nums)
        right_sum.reverse()

        res = []
        for i in range(len(left_sum)):
            res.append(abs(left_sum[i] - right_sum[i]))

        return res

    # partial sum
    # - time: O(n)
    # - space: O(1)
    def leftRigthDifference2(self, nums: List[int]) -> List[int]:
        ans = []
        lsum, rsum = 0, 0
        for num in nums:
            rsum += num
        for num in nums:
            rsum -= num
            print(lsum, rsum)
            ans.append(abs(lsum - rsum))
            lsum += num
        return ans


solution = Solution()
res = solution.leftRigthDifference2([10, 4, 8, 3])
print(res)
