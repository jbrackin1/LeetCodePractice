from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix   #assign result left to right to prefix
            prefix *= nums[i]
        postfix = 1

        for i in range(len(nums) - 1, -1, -1):  #multiply result by postfix on the way back (right to left)
            res[i] *= postfix
            postfix *= nums[i]
        return res