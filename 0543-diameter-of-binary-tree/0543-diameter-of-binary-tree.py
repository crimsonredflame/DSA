# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # we can use maxi[0] or self.maxi or nonlocal maxi
        self.maxi = 0
        def dia(root) :
            if root == None :
                return 0
            lh = dia(root.left)
            rh = dia(root.right)
            self.maxi = max(self.maxi,lh+rh)
            return 1+max(lh,rh)
        dia(root)
        return self.maxi