# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None:
            return None

        if head.next == None:
            return head

        nodeStack = Stack()
        nodeStack.push(head)

        pointer = head.next
        nodeStack.push(pointer)

        while pointer.next != None:
            pointer = pointer.next
            nodeStack.push(pointer)

        nodeStack.print_stack()

        newHead = nodeStack.pop()

        pointer = newHead

        while nodeStack.get_size() > 0:
            nextPointer = nodeStack.pop()
            pointer.next = nextPointer
            pointer = nextPointer

        pointer.next = None

        return newHead


class Stack():

    def __init__(self):
        self.stack = []

    def get_size(self):
        return len(self.stack)

    def push(self, val):
        self.stack.append(val)

    def print_stack(self):
        for i in self.stack:
            print("\n" + str(i.val))

    def pop(self):
        if len(self.stack) > 0:
            val = self.stack[-1]
            del self.stack[-1]
            return val
        return False
