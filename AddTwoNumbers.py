def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def getsum1(node):
            if node.next == None:
                return str(node.val)
            else:
                return  getsum1(node.next) + str(node.val)
        answer = int(getsum1(l1)) + int(getsum1(l2))
        z = y = ListNode(answer % 10)
        answer //= 10
        while answer != 0:
            y.next = y =  ListNode(answer % 10)
            
            answer //= 10
        return z
class ListNode:
    def __init__(self, x):
       self.val = x
       self.next = None
