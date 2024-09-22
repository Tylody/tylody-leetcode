# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root == None and subRoot == None:
            return True

        check_subtree = False
        if root.val == subRoot.val:
            check_subtree = self.check_potential_valid_subtree(root, subRoot)

        if check_subtree:
            return True

        if root.left == None and root.right == None:
            return False

        check_left = False
        check_right = False
        if root.left != None:
            check_left = self.isSubtree(root.left, subRoot)

        if root.right != None:
            check_right = self.isSubtree(root.right, subRoot)

        return check_left or check_right

    def check_potential_valid_subtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root.val != subRoot.val:
            print(str(root.val) + " - " + str(subRoot.val))
            return False

        check_left = True
        check_right = True
        if root.left != None and subRoot.left != None:
            print(str(root.left.val) + " + " + str(subRoot.left.val))
            check_left = self.check_potential_valid_subtree(root.left, subRoot.left)

        if root.right != None and subRoot.right != None:
            print(str(root.right.val) + " + " + str(subRoot.right.val))
            check_right = self.check_potential_valid_subtree(root.right, subRoot.right)

        if root.left == None and subRoot.left != None or root.left != None and subRoot.left == None:
            check_left = False

        if root.right == None and subRoot.right != None or root.right != None and subRoot.right == None:
            check_right = False

        return check_left and check_right
