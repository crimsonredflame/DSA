# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root == None :
            return []
    #     res = []
    #     return self.preorder(root,res)
    # def preorder(self,root,res) :
    #     if root == None :
    #         return
    #     res.append(root.val)
    #     self.preorder(root.left,res)
    #     self.preorder(root.right,res)
    #     return res

        st = []
        res = []
        st.append(root)
        while st :
            ele = st.pop()
            if ele.right :
                st.append(ele.right)
            if ele.left :
                st.append(ele.left)
            res.append(ele.val)
        return res