# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        
        smaller = []
        bigger = []
        for number in preorder[1:]:
            if number < root.val:
                smaller.append(number)
            else:
                bigger.append(number)

        root.left = self.bstFromPreorder(smaller)
        root.right = self.bstFromPreorder(bigger)

        return root