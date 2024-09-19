"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head is None:
            return None

        if head.next is None:
            return Node(head.val, None, head.random)

        pointer = head

        list_of_copied_nodes = []
        list_of_random_values = []

        while pointer != None:
            new_node = Node(pointer.val)
            list_of_copied_nodes.append(new_node)

            if pointer.random != None:
                list_of_random_values.append(pointer.random.val)
            else:
                list_of_random_values.append(None)

            pointer = pointer.next

        print(list_of_copied_nodes)
        print(list_of_random_values)

        random_indexes_dict = {}
        random_indexes_dict[None] = None

        for i in range(len(list_of_copied_nodes) - 1):
            list_of_copied_nodes[i].next = list_of_copied_nodes[i + 1]

        for i in range(len(list_of_random_values)):
            counter = 0
            pointer = head
            while True:
                if list_of_random_values[i] == None:
                    counter = None
                    break
                if pointer.val != list_of_random_values[i]:
                    pointer = pointer.next
                    counter += 1
                    continue
                break

            random_indexes_dict[list_of_random_values[i]] = counter

        print(random_indexes_dict)

        for i in range(len(list_of_random_values)):
            if random_indexes_dict[list_of_random_values[i]] == None:
                list_of_copied_nodes[i].random = None
                continue

            list_of_copied_nodes[i].random = list_of_copied_nodes[random_indexes_dict[list_of_random_values[i]]]

        return list_of_copied_nodes[0]