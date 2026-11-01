class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if root is None:
            return 0

        r1 = self.maxDepth(root.right)
        r2 = self.maxDepth(root.left)

        return 1+max(r1,r2)
        