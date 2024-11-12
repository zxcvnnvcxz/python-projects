from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None  # This will eventually be the new head of the reversed list

        # Traverse through the list and reverse the pointers
        while head:
            next_node = head.next  # Save the next node
            head.next = new_head  # Reverse the pointer of the current node
            new_head = head  # Move the new_head to the current node (the new start of the reversed list)
            head = next_node  # Move to the next node in the original list

        return new_head  # This returns the head of the reversed list, which is now a ListNode

    def reverseListRecursion(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        new_head = self.reverseListRecursion(head.next)

        front = head.next
        front.next = head
        head.next = None

        return new_head


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    solution = Solution()
    reversed_head = solution.reverseList(head)

    original = head
    current = reversed_head

    while current:
        print(current.val, end=" -> ")
        current = current.next