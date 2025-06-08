#1337c0de - Top K Frequent Words
from typing import List
from collections import OrderedDict

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordFrequency = OrderedDict()
        for word in words:
            if word in wordFrequency:
                wordFrequency[word] += 1
            else:
                wordFrequency[word] = 1
        sortedWords = sorted(wordFrequency.items(), key=lambda item: (-item[1], item[0]))
        return [word for word, freq in sortedWords[:k]] #: word for word, ... this is for unpacking tuples :k slice first                                                                          1st k elements from sortedWords
            
            
            