#1337c0de # 269 - Alien Dictionary

from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = { c:set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1,w2 = words[i], words[i + 1] #two adjacent words
            minLen = min(len(w1), len(w2)) #minimum length of either word
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]: #retrieves first three letters, the prefix of both woprds
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]: # build the directed graph representation of the character order based on the comparisons of adjacent words:
                    adj[w1[j]].add(w2[j]) 
                    break
        
        visit = {}
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]

            visit[c] = True #think of visit like processed
            for next_char in adj[c]:
                if dfs(next_char):
                    return True
            visit[c] = False # this is to mark it not visited for the next iteration
            res.append(c)
        
        for c in adj:
            if dfs(c):      
                return ""
                            #if this returns true, it indicates a cycle has been detected, in that case it is impossible 
                            #to deteramine a valid character order due to the prescence of conflicting relationships among characters
        res.reverse()
        return "".join(res)

# Example usage
solution = Solution()
words = ["wrt", "wrf", "er", "ett", "rftt"]
print(solution.alienOrder(words))  # Output: "wertf" or similar valid order