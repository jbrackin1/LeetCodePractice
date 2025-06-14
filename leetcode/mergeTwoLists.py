from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #create a dummy node to help with merging
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        return dummy.next










        list1 = [1,2,4] 
        list2 = [1,3,4]
        print(self.mergeTwoLists(list1, list2))
# # Output: [1,1,2,3,4,4]


# Example 2:

# list1 = [], list2 = []


# # Output: []

# list1 = [], list2 = [0]


# # Output: [0]