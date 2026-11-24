# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return "N"
        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)

        

    def deserialize(self, data):
        self.vals = (data.split(","))
        self.i = 0

        def build():
            val = self.vals[self.i]
            self.i += 1
            
            if val == "N":
                return None
            
            node = TreeNode(int(val))        # convert the string to a number
            node.left = build()            # build the left subtree
            node.right = build()            # build the right subtree
            return node
        
        return build()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))