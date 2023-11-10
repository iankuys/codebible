# Python3 Program for Implementing 
# prefix sum array 
  
# Fills prefix sum array 
  
  
def fillPrefixSum(arr, n, prefixSum): 
  
    prefixSum[0] = arr[0] 
  
    # Adding present element 
    # with previous element 
    for i in range(1, n): 
        prefixSum[i] = prefixSum[i - 1] + arr[i] 
  
  
# Driver code 
if __name__ == '__main__': 
  arr = [10, 4, 16, 20] 
  n = len(arr) 
  
  # Function call 
  prefixSum = [0 for i in range(n + 1)] 
  
  fillPrefixSum(arr, n, prefixSum) 
  
  for i in range(n): 
      print(prefixSum[i], " ", end="") 
  
# This code is contributed 
# by Anant Agarwal. 
  

# Sum of an array between indexes L and R using Prefix Sum:
# Python3 program for the above approach 
  
# Driver code 
if __name__ == '__main__': 
    n = 6
    a = [3, 6, 2, 8, 9, 2] 
    pf = [0 for i in range(n+2)] 
    for i in range(n): 
        pf[i + 1] = pf[i] + a[i] 
  
    q = [[2, 3], [4, 6], [1, 5], [3, 6]] 
    for i in range(4): 
        l = q[i][0] 
        r = q[i][1] 
  
        # Calculating sum from r to l. 
        print(pf[r] - pf[l - 1]) 
  