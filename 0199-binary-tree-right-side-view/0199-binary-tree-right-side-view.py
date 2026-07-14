# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def revPreorder(node,lev,ds) :
            if node == None :
                return 
            if len(ds) == lev : ds.append(node.val)
            revPreorder(node.right,lev+1,ds)
            revPreorder(node.left,lev+1,ds)
        res = []
        revPreorder(root,0,res)
        return res