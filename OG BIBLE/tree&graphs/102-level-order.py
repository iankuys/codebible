# LeetCode Problem 102: https://leetcode.com/problems/
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = [root]
        array = []
        
        while queue and root:
            
            newLevel = []
            subarray = []
            
            for i in queue:
                subarray.append(i.val)
                                           
                if i.left is not None:
                    newLevel.append(i.left)
                    
                if i.right is not None:
                    newLevel.append(i.right)
               

            queue = newLevel
            array.append(subarray)

        
        return array
            
        