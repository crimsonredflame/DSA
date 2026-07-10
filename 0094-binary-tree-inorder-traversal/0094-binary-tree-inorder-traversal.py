# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root == None :
            return []
    #     res = []
    #     return self.inorder(root,res)
        
    # def inorder(self,root,res) :
    #     if root == None :
    #         return
    #     self.inorder(root.left,res)
    #     res.append(root.val)
    #     self.inorder(root.right,res)

    #     return res

        res = []
        st = []
        node = root
        while True :
            if node != None :
                st.append(node)
                node = node.left
            else :
                if not st :
                    break
                node = st.pop()
                res.append(node.val)
                node = node.right
        return res