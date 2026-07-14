# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def isSym(lef,rig) :
            if lef == None or rig == None :
                return lef == rig

            return lef.val == rig.val and isSym(lef.left,rig.right) and isSym(lef.right,rig.left)
        
        return root == None or isSym(root.left,root.right)

        