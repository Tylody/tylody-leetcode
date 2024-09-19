# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        pointer = head
        nodeStack = Stack()

        while pointer != None:
            nodeStack.push(pointer)
            pointer = pointer.next

        if nodeStack.get_size() == n:
            if n == 1:
                return None

            return head.next

        if n == 1:
            nodeStack.pop()
            nodeStack.pop().next = None
            return head

        node_at_n_minus_one = None

        for i in range(n + 1):
            node_at_n_minus_one = nodeStack.pop()

        node_at_n_minus_one.next = node_at_n_minus_one.next.next

        return head


class Stack():

    def __init__(self):
        self.stack = []

    def get_size(self):
        return len(self.stack)

    def push(self, val):
        self.stack.append(val)

    def print_stack(self):
        for i in self.stack:
            print(str(i.val))

    def pop(self):
        if len(self.stack) > 0:
            val = self.stack[-1]
            del self.stack[-1]
            return val
        return False