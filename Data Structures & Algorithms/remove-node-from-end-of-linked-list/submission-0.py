class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        l = 0

        # Pass 1: Count total length
        while curr:
            l += 1
            curr = curr.next
        
        # Edge case: removing the head node
        if l == n:
            return head.next
        
        curr = head
        prev = None
        idx = 0

        # Pass 2: Find the target index to remove
        while curr:
            if idx == (l - n):
                prev.next = curr.next
                return head
            else:
                prev = curr
                curr = curr.next
                idx += 1  # <-- FIXED: Increment idx