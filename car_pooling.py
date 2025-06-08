    #1337c0de #1094 - Car Pooling

import heapq
from typing import List

class Solution():
        def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
            print(trips)
            trips.sort(key = lambda t: t[1])

            minHeap = []
            curPassengers = 0
            for t in trips:
                numPassengers, startLocation, endLocation = t
                while minHeap and minHeap[0][0] <= startLocation:
                    curPassengers -= minHeap[0][1] #remove when the first trip starts
                    heapq.heappop(minHeap)  #remove the last tuple on the heap

                curPassengers += numPassengers #add num passengers from the trip to the current count
                if curPassengers > capacity: #if the current count is greater than capacity
                    return False
                heapq.heappush(minHeap, [endLocation, numPassengers]) #push (to the minHeap) the end Location and numPassengers  adding 1 to the minHeap
            return True


            
            


            
            