# # TREEQUESTions
# # Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return p == q
        return (p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))

            
# # Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            for _ in range(len(q1)):
                nodeP = q1.popleft()
                nodeQ = q2.popleft()

                if nodeP is None and nodeQ is None:
                    continue
                if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                    return False

                q1.append(nodeP.left)
                q1.append(nodeP.right)
                q2.append(nodeQ.left)
                q2.append(nodeQ.right)

        return True
# # # ==============================================================================


from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True  # An empty tree is symmetric

        def isMirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            if not t1 and not t2:
                return True  # Both subtrees are empty
            if not t1 or not t2:
                return False  # One subtree is empty and the other isn't
            return (
                t1.val == t2.val and 
                isMirror(t1.left, t2.right) and 
                isMirror(t1.right, t2.left)
            )

        return isMirror(root.left, root.right)
# ==========================================================================================================
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
    

        return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))

sol =Solution()
print(sol.maxDepth([3,9,20,0,0,15,7]))
# =====================================================================================
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is  None:
            return None
        def checkHeight(self,root):
            if not root:
                return 0

            left = self.checkHeight(root.left)
            right = self.checkHeight(root.right)

            if left < 0 or right < 0 or abs(left-right) > 1:
                return -1
            return max(left,right)+1
        
# =======================================================================================

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:  #corner case
            return 0
        if root.left is None and root.right is None: #base case
            return 1
        if root.left is None:
            return self.minDepth(root.right)+1
        if root.right is None:
            return self.minDepth(root.left)+1
        return min(self.minDepth(root.left),self.minDepth(root.right))+1
    
# using stack better approach
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [root]
        depth = 0

        while stack:
            
            temp = []
            depth +=1
            for node in stack:
                if not node.left and not node.right:
                    return depth

                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            stack = temp
# ===============================================================================
            