from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head and head.next is None:
            return False
        # Initialise two pointers, slow, and fast to the head of the linked list.
        slow = head
        fast = head

        # Traverse linked list with both pointers
        while fast and fast.next is not None:
            slow = slow.next # Move slow one step
            fast = fast.next.next # Move fast two steps

            # Check if slow and fast pointers meet
            if slow == fast:
                return True # Loop detected

        # If fast reaches the end of the list, there is no loop
        return False
