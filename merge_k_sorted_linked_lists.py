# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        print(lists)

        if lists == None:
            return None

        if lists == []:
            return None

        all_empty_lists = True
        for i in lists:
            if i != []:
                all_empty_lists = False
                break
        if all_empty_lists: return None

        merged_list = []

        while True:
            merging_lists = []
            merging_lists_id = []
            for i in range(len(lists)):
                if lists[i] != None:
                    merging_lists.append(lists[i])
                    merging_lists_id.append(i)

            if len(merging_lists) == 0:
                break

            minimum = float('inf')
            list_id = -1
            for i in range(len(merging_lists)):
                if merging_lists[i].val < minimum:
                    minimum = merging_lists[i].val
                    list_id = i

            merged_list.append(merging_lists[list_id])
            lists[merging_lists_id[list_id]] = lists[merging_lists_id[list_id]].next

            for i in range(len(merged_list) - 1):
                merged_list[i].next = merged_list[i + 1]

        merged_list[-1].next = None

        print(lists)

        return merged_list[0]