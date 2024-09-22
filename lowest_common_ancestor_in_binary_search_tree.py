# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if p.val == root.val:
            return p

        if q.val == root.val:
            return q

        parents_found = {}

        parents_found[p.val] = p
        parents_found[q.val] = q

        while True:
            print(parents_found)
            p = self.find_parent(root, p)
            q = self.find_parent(root, q)

            if parents_found.get(q.val, None) != None and q.val != root.val:
                return q
            parents_found[q.val] = q

            if parents_found.get(p.val, None) != None and p.val != root.val:
                return p
            parents_found[p.val] = p

            if q.val == root.val and p.val == root.val:
                return root

    def find_parent(self, root: TreeNode, target: TreeNode) -> TreeNode:

        if root.val == target.val:
            return root

        if root.left == None and root.right == None or target == None:
            return None

        if root.left != None and root.left.val == target.val:
            return root

        if root.right != None and root.right.val == target.val:
            return root

        left_contains = None
        right_contains = None

        if root.left != None:
            left_contains = self.find_parent(root.left, target)

        if root.right != None:
            right_contains = self.find_parent(root.right, target)

        if left_contains != None: return left_contains
        if right_contains != None: return right_contains