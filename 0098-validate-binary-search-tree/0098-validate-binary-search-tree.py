# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def res(node,low,hig) :
            if node == None :
                return True
            return low < node.val and hig > node.val and res(node.left,low,node.val) and res(node.right,node.val,hig)
        return res(root,float('-inf'),float('inf'))
        