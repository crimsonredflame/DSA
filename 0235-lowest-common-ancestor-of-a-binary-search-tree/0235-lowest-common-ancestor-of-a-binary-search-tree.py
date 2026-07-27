# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        curr = root
        while (curr.val < p.val and curr.val < q.val) or (curr.val > p.val and curr.val > q.val) :
            if curr.val < p.val and curr.val < q.val :
                curr = curr.right
            if curr.val > p.val and curr.val > q.val :
                curr = curr.left
        return curr