# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head == None:
            return False

        if head.next == None:
            return False

        pointer = head
        list_of_nodes = []
        while True:

            for i in list_of_nodes:
                if i is pointer:
                    return True

            list_of_nodes.append(pointer)

            if pointer.next == None:
                return False

            pointer = pointer.next