# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        
        def treemake(preorder, inorder,prestart,preend,instart,inend) :
            if prestart > preend or instart > inend :
                return
            
            for i in range(instart,inend+1) :
                if inorder[i] == preorder[prestart] :
                    idx = i
            numLeft = idx - instart
            tree = TreeNode()
            tree.val = preorder[prestart]
            tree.left = treemake(preorder,inorder,prestart + 1 , prestart + numLeft, instart, idx-1 )
            tree.right = treemake(preorder,inorder, prestart+numLeft+1, preend , idx + 1, inend)
            return tree
        return treemake(preorder,inorder,0,len(preorder) - 1,0,len(inorder) - 1)