
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def recursiveFunc(node, depth):
            if not node:
                return
            if depth == len(ans):
                ans.append(node.val)
            recursiveFunc(node.right, depth+1)
            recursiveFunc(node.left, depth+1)

            
        recursiveFunc(root, 0)
        return ans