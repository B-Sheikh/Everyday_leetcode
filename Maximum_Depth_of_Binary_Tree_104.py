class Solution(object):
    def maxDepth(self, root):
        def dep(root):
            if root is None:
                return 0

            lde = dep(root.left)
            rde = dep(root.right)

            return max(lde, rde) + 1

        return dep(root)
