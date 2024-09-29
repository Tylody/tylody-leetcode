# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if root == None:
            return True

        if root.left == None and root.right == None:
            return True

        validity = self.check_validity(root, float('inf') * (-1), float('inf'))

        return validity

    def check_validity(self, root, limit_min, limit_max):

        check_left = True
        check_right = True

        print("BOBO")
        print(root.val, " ", limit_min, " ", limit_max)
        if root.left != None and root.right != None:
            print(root.val, " ", root.left.val, " ", root.right.val)

        if root.left != None:
            if root.left.val >= root.val:
                print("FLAG 1")
                check_left = False

            if root.left.val <= limit_min:
                print("FLAG 2")
                check_left = False

        if root.right != None:
            if root.right.val <= root.val:
                print("FLAG 3")
                check_right = False

            if root.right.val >= limit_max:
                print("FLAG 4")
                check_right = False

        if check_left and check_right:
            print("FLAG 5")
            check_children_left = True
            check_children_right = True

            if root.left != None:
                check_children_left = self.check_validity(root.left, limit_min, root.val)

            if root.right != None:
                check_children_right = self.check_validity(root.right, root.val, limit_max)

            return check_children_left and check_children_right

        else:
            return False

