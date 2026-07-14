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
        p1,q1 = [],[]
        def path(node,tar,arr) :
            if node == None :
                return False
            arr.append(node)
            if node.val == tar.val :
                return True
            if path(node.left,tar,arr) or path(node.right,tar,arr) :
                return True
            arr.pop()
        path(root,p,p1)
        path(root,q,q1)
        l = min(len(p1),len(q1))
        res = 0
        for i in range(l) :
            if p1[i].val == q1[i].val :
                res = p1[i]
            else :
                break
        return res
        

            