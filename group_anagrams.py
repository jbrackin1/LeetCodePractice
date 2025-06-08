from typing import List
from collections import defaultdict
#1337c0de # 49 - Group Anagrams
#use a hash map or OrderedDict in Python?
#they use a regular Dict
#big O(n * k)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 #a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1 #subtract ascii value "a" from ascii value of char

            res[tuple(count)].append(s)

        return list(res.values())