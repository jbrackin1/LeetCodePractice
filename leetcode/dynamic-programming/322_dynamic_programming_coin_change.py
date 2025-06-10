from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # print(coins)
        # print(amount)
        #Lets take a dynamic programming Bottom Up approach to this the value is the number of coins to research the index
        #5, 5, 1
        #DP[5] = 1
        #DP [1] = 1
        #DP [0] = 0
        #DP[2] = 1
        #DP[3] = 2
        #DP[4] = 2
        #DP[6] = 2
        dp = [amount + 1] * (amount + 1)
        print(dp)
        #base case
        dp[0] = 0
        for amt in range(1, amount + 1):
            for c in coins:
                if amt - c >= 0:
                    dp[amt] = min(dp[amt], 1 + dp[amt - c]) #amt is 1 to 12 this is called the recurrence relation
        return dp[amount] if dp[amount] != amount + 1 else -1

coins1 = [1,2,5] 
amount1 = 11
coins2 = [2] 
amount2 = 3
coins3 = [1] 
amount3 = 0
solution = Solution()
print(solution.coinChange(coins1, amount1)) #3
print(solution.coinChange(coins2, amount2)) #-1
print(solution.coinChange(coins3, amount3)) #0

#Time O(amount * len(coins))
#Space O(amount)

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0
