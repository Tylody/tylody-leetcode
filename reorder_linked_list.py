# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if head == None:
            return

        if head.next == None:
            return

        nodeStack = Stack()
        nodeStack.push(head)

        pointer = head.next
        nodeStack.push(pointer)

        while pointer.next != None:
            pointer = pointer.next
            nodeStack.push(pointer)

        linked_list_size = nodeStack.get_size()

        odd_number_size = linked_list_size % 2 == 1

        arrayOfNodes = nodeStack.stack

        nodeStack.print_stack()

        for i in range(linked_list_size // 2):
            frontwards_index = i
            backwards_index = -i - 1

            arrayOfNodes[frontwards_index].next = arrayOfNodes[backwards_index]
            arrayOfNodes[backwards_index].next = arrayOfNodes[frontwards_index + 1]

        middle_index = linked_list_size // 2
        arrayOfNodes[middle_index].next = None

        return


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