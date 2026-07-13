# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root == None :
            return 0
        dq = deque()
        dq.append((root,0))
        res = 1
        while dq :
            minm = dq[0][1]
            size = len(dq)
            for i in range(size) :
                node,val = dq.popleft()
                mul = val-minm
                if i == 0 : left = val
                if i == size-1 : right = val
                if node.left : dq.append((node.left,2*mul+1))
                if node.right : dq.append((node.right,2*mul+2))
            res = max(res,right-left+1)
        return res