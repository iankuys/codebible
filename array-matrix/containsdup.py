class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}

        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                return True
        return False
    
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset = set()

        for num in nums:
            if num not in numset:
                numset.add(num)
            else:
                return True
        return False