# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        def isLeaf(node) :
            return node.left == None and node.right == None 
        self.res = []
        def binary(node,arr) :
            if node == None :
                return
            arr.append(node.val)
            if isLeaf(node) : 
                self.res.append("->".join(map(str, arr)))
            binary(node.left,arr)
            binary(node.right,arr)
            arr.pop()
        binary(root,[])
        return self.res