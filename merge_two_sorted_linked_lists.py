# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # edge cases
        if list1 == None and list2 == None:
            return None

        if list2 == None:
            return list1

        if list1 == None:
            return list2

        newList = None

        if list1.val == list2.val or list1.val < list2.val:
            newList = ListNode(list1.val)
            list1 = list1.next

        elif list2.val < list1.val:
            newList = ListNode(list2.val)
            list2 = list2.next

        pointer = newList

        while True:
            if list1 == None and list2 == None:
                return newList

            if list1 == None:
                while list2 != None:
                    pointer.next = list2
                    list2 = list2.next
                    pointer = pointer.next

            if list2 == None:
                while list1 != None:
                    pointer.next = list1
                    list1 = list1.next
                    pointer = pointer.next

            elif list1.val == list2.val or list1.val < list2.val:
                pointer.next = list1
                list1 = list1.next
                pointer = pointer.next

            elif list2.val < list1.val:
                pointer.next = list2
                list2 = list2.next
                pointer = pointer.next



