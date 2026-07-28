# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):
    st = []
    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.st = []
        
        while root :
            self.st.append(root)
            root = root.left

    def next(self):
        """
        :rtype: int
        """
        ele = self.st.pop()
        val = ele.val
        if ele.right :
            ele = ele.right
            while ele :
                self.st.append(ele)
                ele = ele.left
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.st)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()