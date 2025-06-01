# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Link: https://leetcode.com/problems/top-k-frequent-elements/

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

class Solution:
    # Time Complexity:
    #   Best case: O(n²) - nested iteration
    #   Average case: O(n²)
    #   Worst case: O(n²)
    # Space Complexity: O(1)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ele_dict = {}
        output = []
        for num in nums:
            if num not in ele_dict:
                ele_dict[num] = 1
            else:
                ele_dict[num] += 1

        ele_dict = {key: value for key, value in sorted(ele_dict.items(), reverse=True, key=lambda item: item[1])}

        print(ele_dict)
        for key, value in ele_dict.items():
            if k > 0:
                print(k)
                print(key)
                output.append(key)
                k -= 1
            else:
                break
        
        return output
            
class Solution:
    # Time Complexity:
    #   Best case: O(n²) - nested iteration
    #   Average case: O(n²)
    #   Worst case: O(n²)
    # Space Complexity: O(1)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num) 
                if len(res) == k:
                    return res       
    
# arr = [[3,1], [2,2], [1,3]]
# arr.sort()  # sorts to [[1,3], [2,2], [3,1]]
class Solution:
    # Time Complexity:
    #   Best case: O(n²) - nested iteration
    #   Average case: O(n²)
    #   Worst case: O(n²)
    # Space Complexity: O(1)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res