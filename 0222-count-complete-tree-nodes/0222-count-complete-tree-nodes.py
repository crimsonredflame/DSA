# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root == None :
            return 0
        lh,rh = 0,0
        temp = root
        while temp :
            temp = temp.left
            lh +=1
        temp = root
        while temp :
            temp = temp.right
            rh +=1

        if lh == rh : return 2**lh - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)