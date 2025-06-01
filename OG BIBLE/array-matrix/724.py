# LeetCode Problem 724: https://leetcode.com/problems/
#Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1.

def pivotIndex(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def findPivot(nums):
            SUM = sum(nums)
            leftSum = 0
            print(SUM)
                        
            for i, j in enumerate(nums):
                if(leftSum == SUM - j - leftSum):
                    return i
                leftSum += j
                
            return -1
            
        return findPivot(nums)
            

array = [1,7,3,6,5,6]
array2 = [-1,-1,-1,1,1,1]
print(pivotIndex(array))                    
                