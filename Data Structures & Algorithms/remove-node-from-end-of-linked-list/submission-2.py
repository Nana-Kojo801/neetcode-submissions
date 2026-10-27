class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        l = 0

        while curr:
            l += 1
            curr = curr.next
        
        if l == n:
            return head.next
        
        curr = head
        prev = None
        idx = 0

        while curr:
            if idx == (l - n):
                prev.next = curr.next
                return head
            else:
                prev = curr
                curr = curr.next
                idx += 1