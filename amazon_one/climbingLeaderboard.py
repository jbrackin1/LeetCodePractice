def climbingLeaderboard(ranked, player):
    # unique_ranks = sorted(set(ranked), reverse=True)
    result = []
    unique_ranks = sorted(set(ranked), reverse = True) #sets take out duplicates, meaning same length and indices
    index = len(unique_ranks) - 1
    
    for score in player:
        while index > -1 and score >= unique_ranks[index]:
            index -= 1
        result.append(index + 2)
    return result

ranks = [100, 100, 50, 40, 40, 20, 10]
player_scores = [5 ,25, 50, 120]

print(climbingLeaderboard(ranks, player_scores)) # Should output 6 4 2 1

#search and ranking problems