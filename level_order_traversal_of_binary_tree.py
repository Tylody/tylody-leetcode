# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root == None:
            return []

        level_order_traversal = []
        i = 0
        depth = self.find_depth(root)

        while depth - i > 0:
            current_list = self.clear_level(depth - i - 1, root)

            level_order_traversal.append(current_list)

            i += 1

        level_order_traversal.reverse()
        return level_order_traversal

    def clear_level(self, levels, root):

        list_nodes = []
        left_nodes = []
        right_nodes = []

        if levels > 0:
            if root.left != None:
                left_nodes = self.clear_level(levels - 1, root.left)

            if root.right != None:
                right_nodes = self.clear_level(levels - 1, root.right)

        for i in left_nodes:
            list_nodes.append(i)

        for i in right_nodes:
            list_nodes.append(i)

        if levels == 0:
            list_nodes.append(root.val)

        return list_nodes

    def find_depth(self, root):

        counter_left = 1
        counter_right = 1

        if root.left != None:
            counter_left += self.find_depth(root.left)

        if root.right != None:
            counter_right += self.find_depth(root.right)

        if root.left == None and root.right == None:
            return 1

        return max(counter_left, counter_right)