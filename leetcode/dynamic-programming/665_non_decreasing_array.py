from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        changed = False
        for i in range(len(nums) - 1):   #if it were just the array it would be len(nums) but since we are checking pairs its len(nums) - 1
            if nums[i] <= nums[i + 1]:
                continue
            if changed:
                return False
            #we want to decrease the left element here
            #if the number value before the number value at i is greater than the number value after the current value at i 
            #set the number value before i to the one after i
            if i == 0 or nums[i - 1] <= nums[i + 1]:
                nums[i] = nums[i + 1]
            else:
                nums[i + 1] = nums[i]
            changed = True
        return True
