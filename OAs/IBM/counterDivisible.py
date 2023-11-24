from collections import Counter

def solve(nums, d):
    n = len(nums)
    counter = Counter()
    res = 0
    for j in range(n-2,-1,-1):
        counter[nums[j+1]%d] += 1

        for i in range(j):
            res += counter[-(nums[i]+nums[j])%d] 
            print(res, -(nums[i]+nums[j])%d)

    return res

print(solve([3,3,4,7,8], 5))

from collections import defaultdict
import bisect

def find_triplets(nums, d):
    n = len(nums)
    dic = defaultdict(list)
    for i in range(n):
        x = nums[i] % d
        dic[x].append(i)
    count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            cur_mod = (nums[i] + nums[j]) % d
            search_mod = (d - cur_mod) % d
            index = bisect.bisect_left(dic[search_mod], j + 1)
            count += len(dic[search_mod]) - index
    return count

assert find_triplets([3, 3, 4, 7, 8], 5) == 3