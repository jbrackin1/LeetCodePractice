from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = { 0 : 1}

        for total in range(1, 1 + target):
            dp[total] = 0 
            for num in nums:
                dp[total] += dp.get(total - num, 0)
        return dp[target]

solution = Solution()
nums = [1,2,3] 
target = 4
print(solution.combinationSum4(nums, target))
