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
        res = []
        def binary(node,path) :
            if node == None :
                return
            path += str(node.val)
            if isLeaf(node) : 
                res.append(path)
            path += '->'
            binary(node.left,path)
            binary(node.right,path)
        binary(root,"")
        return res