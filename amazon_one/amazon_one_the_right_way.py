import heapq

def count_possible_winners_with_heap(initialRewards):
    count = 0
    n = len(initialRewards)

    # Create a max-heap (invert values for min-heap behavior)
    max_heap = [-reward for reward in initialRewards] #Inverted min heap,effectively a max heap
    heapq.heapify(max_heap)

    # Get the maximum score from the heap
    max_score = -max_heap[0]  # This is the maximum score among all players 

    # Count how many players have the maximum score
    max_count = initialRewards.count(max_score)

    for i in range(n):
        # Calculate current player's total points
        current_total = initialRewards[i] + n

        # Compare with the maximum score of others
        if current_total >= max_score:
            # If the current player's score is equal to the max score,
            # we need to ensure that they are not the only one with that score.
            if current_total > max_score or max_count > 1:
                count += 1

    return count

# Test the function
print(count_possible_winners_with_heap([1, 3, 4]))  # Expected Output: 2

#Best Time Space Complexity 
# Time Complexity: O(n)
# Space Complexity: O(n)

