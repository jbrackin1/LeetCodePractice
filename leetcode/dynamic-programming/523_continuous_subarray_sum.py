from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0 : -1} #map remaining to ending index
        prefix = 0 
        
        for i,n in enumerate(nums):
            prefix += n
            r = prefix % k
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                return True
        return False

solution = Solution()
nums = [23,2,4,6,7] 
k = 6
print(solution.checkSubarraySum(nums, k))

nums = [23,2,6,4,7] 
k = 6
print(solution.checkSubarraySum(nums, k))

nums = [23,2,6,4,7] 
k = 13
print(solution.checkSubarraySum(nums, k))