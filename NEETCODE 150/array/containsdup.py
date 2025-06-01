class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear scan
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}

        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                return True
        return False
    
class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear scan
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset = set()

        for num in nums:
            if num not in numset:
                numset.add(num)
            else:
                return True
        return False