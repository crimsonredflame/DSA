# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if root == None :
            return TreeNode(val)
        temp = root
        node = None
        while True :
            if temp.val > val :
                if temp.left : temp = temp.left
                else : 
                    temp.left = TreeNode(val)
                    break
            else :
                if temp.right : temp = temp.right
                else : 
                    temp.right = TreeNode(val)
                    break
        return root
            