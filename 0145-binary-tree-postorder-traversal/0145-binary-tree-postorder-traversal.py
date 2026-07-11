# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root == None :
            return []
    # Recursive solution
    #     res = []
    #     return self.postorder(root,res)
    # def postorder(self,root,res) :
    #     if root == None :
    #         return
    #     self.postorder(root.left,res)
    #     self.postorder(root.right,res)
    #     res.append(root.val)
    #     return res

    # 2 stacks iterative solution
        st1 = []
        st2 = []
        st1.append(root)
        res = []
        while st1 :
            ele = st1.pop()
            if ele.left :
                st1.append(ele.left)
            if ele.right :
                st1.append(ele.right)
            st2.append(ele)
        while st2 :
            res.append(st2.pop().val)
        return res
