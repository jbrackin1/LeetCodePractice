from typing import List
from collections import OrderedDict
from typing import List
from collections import OrderedDict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_frequency = OrderedDict()
        for num in nums:
            if num in num_frequency:
                num_frequency[num] += 1
            else:
                num_frequency[num] = 1
            if num_frequency[num] > 1:
                return True
        return False
        

solution = Solution()
print(solution.containsDuplicate([1,2,3,3]))
print(solution.containsDuplicate([1,2,3,4]))
print(solution.containsDuplicate([1,1,2]))