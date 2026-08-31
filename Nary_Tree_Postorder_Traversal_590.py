"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        l = []
        def posor(node):
            if not node:
                return
            for i in node.children:
                posor(i)    
            x = node.val
            l.append(x)
        posor(root)
        return l
        
