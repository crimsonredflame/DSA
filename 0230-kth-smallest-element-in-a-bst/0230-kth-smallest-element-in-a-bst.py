# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        st = []
        count = 0
        while True :
            if root != None :
                st.append(root)
                root = root.left
            else :
                if not st :
                    break
                else :
                    ele = st.pop()
                    count+=1
                    if count == k :
                        return ele.val
                    root = ele.right