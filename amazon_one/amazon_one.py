# def count_possible_winners(initialRewards):
#     # n = len(initialRewards)
#     count = 0
#     print(initialRewards)
#     initialRewards.sort(reverse=True)
#     print(initialRewards)
#     for i in range(len(initialRewards)):
#         # The points this customer would get if they win
#         # winner_points = len(initialRewards)
#         current_total = initialRewards[i] + len(initialRewards)

#         # Remaining players and their initial rewards (exclude current)
#         others = initialRewards[:i] + initialRewards[i+1:] #Up to and after (excluding) current element
#                                                             #“Create a new list that includes everything except the ith element.”
#                                                             # Big O(n) for each iteration

#         # Assign points: n-1 down to 1
#         other_total = [others[j] + (len(initialRewards) - j - 1) for j in range(len(initialRewards) - 1)] # -1 because others will always have 1 fewer element

#         if current_total >= max(other_total):
#             count += 1

#     return count

# print(count_possible_winners([1, 3, 4]))  # Output: 2 
# 1 + 3 = 4, 3 + 3 =6, 4 + 3 = 7
# 1 + 2 = 3, 3 + 2 = 5, 4 + 2 = 6
# 1 + 1 = 2, 3 + 1 = 3, 4 + 1 = 5
# max = 4,    max = 6,    max = 7 


# Space for others List: The others list takes O(n) space.
# Space for other_total List: The other_total list also takes O(n) space.
# Other Variables: The space used for variables like count, winner_points, and current_total is O(1).
# Thus, the overall space complexity is:

# O(n)

# Summary
# Time Complexity: O(n 
# 2
#  logn)
# Space Complexity: O(n)

#Most like these hackerrank questions "The Maximum Subarray": While this problem focuses on finding the maximum sum of a contiguous subarray, it often involves comparisons and rankings of values.
# "Climbing the Leaderboard": This problem involves determining how players rank on a leaderboard based on their scores, which is conceptually similar to determining potential winners based on their scores and placements.
# "Sales by Match": This problem requires counting occurrences and comparing values, which can relate to determining how many customers can potentially win based on their scores.
# "Equal": This problem involves determining how many operations are needed to make all elements equal, which can involve similar logic of comparing and ranking values.
def count_possible_winners(initialRewards):
    n = len(initialRewards)
    arr = sorted(initialRewards, reverse=True)
    count = 0

    for i in range(n):
        current_total = arr[i] + n
        max_other = float('-inf')
        k = 0
        for j in range(n):
            if j == i:
                continue
            total = arr[j] + (n - 1 - k)
            if total > max_other:
                max_other = total
            k += 1
        if current_total >= max_other:
            count += 1

    return count
print(count_possible_winners([1, 3, 4]))  # Output: 2 


#this should have been a fucking heap
