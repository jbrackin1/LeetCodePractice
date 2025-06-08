#1337c0de #146 - LRU Cache
#Number 2 most common FAANG in 2022

from collections import OrderedDict

# notes - orderedDict()
class LRUCache(OrderedDict):
    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self:
            self.move_to_end(key) #orderedDict function
            return self[key]
        else:
            return -1
        
    def put(self, key:int, value:int) -> None:
        self[key] = value

        if len(self) > self.capacity:
            self.popitem(last=False)

        self.move_to_end(key)
    
