from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goalpost = len(nums) - 1  #last index of the nums array
        for i in range(len(nums) - 1, -1, -1): #this starts at last index and works it's way to the beginning in a range loop
            if i + nums[i] >= goalpost:
                goalpost = i      #if we can reach the goal update the goal to position i  bringing it closer in 
        return True if goalpost == 0 else False

test = [2,3,1,1,4]
solution = Solution()
print(solution.canJump(test))

test2 = [3,2,1,0,4]
print(solution.canJump(test2))

# Asymptotic optimization (Slightly Faster for certain cases)
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         goalpost = len(nums) - 1  # last index of the nums array
#         for i in range(len(nums) - 1, -1, -1):
#             if i + nums[i] >= goalpost:
#                 goalpost = i  # update the goal to position i
#             if goalpost == 0:  # Early exit condition
#                 return True
#         return goalpost == 0  # If we reach the first index, it's possible this is ternary style with truthy implementation
