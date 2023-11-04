# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

class Solution:
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
            

        