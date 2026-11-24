# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode | None:
        pairs = []
        i = 0

        while i < len(traversal):
            depth = 0 
            while traversal[i] == "-":
                depth += 1
                i += 1
            
            num = 0
            while i < len(traversal) and traversal[i].isdigit():
                num = num * 10 + int(traversal[i])
                i += 1
            
            pairs.append((depth, num))

        self.j = 0
        def build(depth):

            if self.j == len(pairs) or pairs[self.j][0] != depth:
                return None
            
            d, val = pairs[self.j]
            self.j += 1

            node = TreeNode(val)
            node.left = build(depth + 1)
            node.right = build(depth + 1)
            return node
        
        return build(0)

