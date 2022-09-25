#pivot
def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def findPivot(nums):
            SUM = sum(nums)
            leftSum = 0
                        
            for i, j in enumerate(nums):
                if(leftSum == SUM - j - leftSum):
                    return i
                leftSum += j
                
            return -1
            
        return findPivot(nums)
            

array = [1,7,3,6,5,6]
array2 = [-1,-1,-1,1,1,1]
print(pivotIndex(array))                    
                