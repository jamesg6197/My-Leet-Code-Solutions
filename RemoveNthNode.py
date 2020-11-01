def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count = 0
        p = head
        while p != None:
            count+=1
            p = p.next
        z = head
        zprev = head
        for i in range(count - n):
            if i != 0:
                zprev = zprev.next
            z = z.next
        if n == count:
            head = head.next
            
        zprev.next = z.next
        return head
