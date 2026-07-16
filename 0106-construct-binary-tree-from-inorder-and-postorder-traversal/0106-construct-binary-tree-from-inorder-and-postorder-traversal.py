# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        def makeTree (inorder, postorder, instart, inend, poststart,postend) :
            if instart > inend or poststart > postend :
                return
            for i in range(instart,inend + 1) :
                if inorder[i] == postorder[postend] : idx = i
        
            tree = TreeNode()
            tree.val = postorder[postend]
            elelef = idx - instart
            tree.left = makeTree(inorder,postorder,instart,idx-1,poststart, poststart + elelef - 1)
            tree.right = makeTree(inorder,postorder,idx+1, inend, poststart + elelef , postend-1)
            return tree
        return makeTree(inorder, postorder,0,len(inorder)-1,0,len(postorder)-1)