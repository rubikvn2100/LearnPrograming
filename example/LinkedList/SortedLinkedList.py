from typing import Optional
from ListNode import ListNode

class SortedLinkedList:
    def __init__(self) -> None:
        self.head = None

    def isEmpty(self) -> bool:
        return self.head == None
    
    def insert(self, val: int) -> None:
        newNode = ListNode(val)

        q = None
        p = self.head
        while p and p.val < val:
            q = p
            p = q.next

        newNode.next = p

        if not q:
            self.head = newNode
        else:
            q.next = newNode

    def find(self, val: int) -> Optional[ListNode]:
        p = self.head
        while p and p.val < val:
            p = p.next

        if not p:
            return None
    
        if val < p.val:
            return None
        
        return p
    
    def remove(self, val: int) -> bool:
        q = None
        p = self.head
        while p and p.val < val:
            q = p
            p = p.next

        if not p:
            return False
    
        if val < p.val:
            return False
        
        if not q:
            self.head = p.next
        else:
            q.next = p.next
        
        return p

    def show(self) -> None:
        print("Value in the Linked List are: ", end = '')

        p = self.head
        while p:
            print(p.val, end = ' ')
            p = p.next
        
        print()