# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        maxi = [float('-inf')]
        def Path(root,maxi) :
            if root == None :
                return 0
            # lh = max(0,Path(root.left,maxi))
            # rh = max(0,Path(root.right,maxi))
            lh = Path(root.left,maxi)
            rh = Path(root.right,maxi)
            maxi[0] = max(maxi[0],lh+rh+root.val)
            if root.val + max(lh,rh) < 0 :
                return 0
            return root.val + max(lh,rh)
        Path(root,maxi)
        return maxi[0]