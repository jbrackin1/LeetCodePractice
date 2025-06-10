from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        noDupes = set()
        size = len(nums)
        l = 0

        while l < size:
            noDupes.add(nums[l])
            l += 1

        arr = sorted(noDupes)
        k = len(arr)

        # Overwrite the first k elements of nums with unique sorted values
        # Overwrite nums itself A.K.A (in place)
        for i in range(k):
            nums[i] = arr[i]

        return k
# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).