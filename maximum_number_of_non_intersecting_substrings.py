class Solution:
    def maxSubstrings(self, word: str) -> int:
        word_length = len(word)
        n = word_length
        intervals = []

        for i in range(word_length):
            for j in range(i + 3, n):
                if word[i] == word[j]:
                    intervals.append((i, j))
        intervals.sort(key = lambda interval: interval[1]) #ending intaval if tuple is (3,6) this would be 6

        count = 0
        last_end = -1

        for start, end in intervals:
            if start > last_end:
                count += 1
                last_end = end
        return count
    
    #Solved using a Greedy Algorithm