class Solution:
    def EditDistance(self, word1: str, word2: str) -> int:
        # Create a 2D cache initialized to 0
        cache = [[0] * (len(word2) + 1) for i in range(len(word1) + 1)]

        # Fill the first row and first column
        for j in range(len(word2) + 1):
            cache[0][j] = j  # If word1 is empty, we need j operations to convert "" to word2[:j]
        for i in range(len(word1) + 1):
            cache[i][0] = i  # If word2 is empty, we need i operations to convert word1[:i] to ""

        # Fill the cache
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    cache[i][j] = cache[i - 1][j - 1]  # No operation needed
                else:
                    cache[i][j] = 1 + min(
                        cache[i - 1][j],    # Deletion
                        cache[i][j - 1],    # Insertion
                        cache[i - 1][j - 1] # Replacement
                    )

        return cache[len(word1)][len(word2)]  # The edit distance is in the bottom-right cell

# Example usage
solution = Solution()
print(solution.EditDistance("horse", "ros"))  # Output: 3 rorse => rose => ros (delete e)