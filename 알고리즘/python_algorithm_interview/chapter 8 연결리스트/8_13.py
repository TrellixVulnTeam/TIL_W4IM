# sol 1
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(self, head: ListNode) -> bool:
    q: List = []
    if not head:
        return True
    
    node = head
    # 리스트 변환
    while node is not None:
        q.append(node.val)
        node = node.next
    
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False
    
    return True