from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        position = []
        for i in range(len(nums)):
            # if nums[i] != target:
            #     return [-1,-1]
            if nums[i] == target:
                position.append(i)
        if not position:
            return [-1, -1]
        return position
# sol = Solution()
# print(sol.searchRange([5,7,7,8,8,10], 8))
        