# LeetCode Problem 1: https://leetcode.com/problems/
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binaryFind(array, low, high, target):
            low = 0
            mid = 0
            while(low <= high):
                mid = ((low+high)//2)
                print(f'Array[mid]: {array[mid]}')

                if (array[mid] > target):
                    high = mid-1
                elif (array[mid] < target):
                    low = mid+1
                else:
                    return mid
            return -1

        def findIndexes(nums, indexToCheck):
            for i in range(0, indexToCheck):
                count = i+1
                sum = 0
            
                while (count < indexToCheck):
                    sum = 0
                    sum = temp[i] + temp[count]

                    if sum == target:
                        return [i, count]
                        
                    count = count + 1
            return [-1, -1]
            

        if (target != 0):
            temp = nums.copy()
            temp.append(target)
            sortedAns = []
            temp.sort()
            print(f'Temp: {temp}')
        
            indexToCheck = binaryFind(temp, 0, len(temp)-1, target)
            print(f'IndexToCheck: {indexToCheck}')

            sortedAns = findIndexes(nums, indexToCheck)
           
            print(sortedAns[0], sortedAns[1])
            print(f'Original: {nums}')
            print(f'Looking for: {temp[sortedAns[0]],temp[sortedAns[1]]}')

            if(temp[sortedAns[0]] == temp[sortedAns[1]]):
                x = nums.index(temp[sortedAns[0]])
                return (x, nums.index(temp[sortedAns[1]], x+1))
            else:
                return [nums.index(temp[sortedAns[0]]), nums.index(temp[sortedAns[1]])]

        else:
            return [nums.index(temp[sortedAns[0]]), nums.index(temp[sortedAns[1]])]


nums = [-3,4,3,90]
target = 0
ans = []

ans = twoSum(nums, target)
print(ans)




    