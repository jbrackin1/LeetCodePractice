#1337c0de 217 Contains Duplicates

from typing import List

class Solution:
    def contains_duplicate(self, nums:List[int]) -> bool:
        integer_test_set = set()
        for number in nums:
            if number in integer_test_set:
                return True      #If there is a single duplicate return True, otherwise False
            integer_test_set.add(number)
        return False


nums = [1,2,3,4,5]
solution = Solution()
print(solution.contains_duplicate(nums))
        
#My solution hinges on the fact that sets can not contain duplicate values
#If the set contains the number, the program immediately returns True
#If upon adding all of the numbers nothing hits True the program returns False
        #Time Complexity
#    O(1) for hash set
#    Going over entire input number List is O(n) in the worst case scenario
#    O(1) * O(n) = O(n)
#
# 
    # Space Complexity
        #O(n) from the Hash Set
 