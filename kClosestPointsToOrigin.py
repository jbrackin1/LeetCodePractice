# 973. K Closest Points to Origin

from typing import List
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        distances = []

        for x, y in points:
            distance = sqrt(x ** 2 + y**2)
            distances.append([distance, x, y])
        #sort in descending order so - and also want to look at index 0 for each element (the distance)
        #this is so the smallest distances can be popped off the end making it easier to access them 
        distances.sort(key = lambda x:(-x[0]))
        #represents the points left to add
        while k > 0:
        #pop smallest distances (because of the descnding order)
        #add to the result array as just points
            distance, x, y = distances.pop()
            result.append([x,y])
            k -= 1 #move to the next
        return result
        