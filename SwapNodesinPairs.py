def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        ptr = head.next
        head.next = self.swapPairs(head.next.next)
        ptr.next = head
        return ptr
