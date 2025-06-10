from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans
    
test1 = [1,2,3]
test2 = [3,4,7]
solution = Solution()
print(solution.getConcatenation(test1))
print(solution.getConcatenation(test2))
