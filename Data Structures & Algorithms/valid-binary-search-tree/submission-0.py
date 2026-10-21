# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack, isValid = [], True

        def inOrder(node):
            nonlocal isValid
            if not node:
                return
            else:
                inOrder(node.left)
                if stack and stack[-1] >= node.val:
                    isValid = False
                stack.append(node.val)
                inOrder(node.right)
        
        inOrder(root)

        return isValid