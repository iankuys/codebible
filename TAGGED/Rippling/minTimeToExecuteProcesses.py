"""
Question 2: There are n processes to be executed, and the iᵗʰ process has a size of processSize[i], where 1 ≤ i ≤ n. Also, there are m processors of different size capacity. The capacity of the iᵗʰ processor is capacity[i] ( 1 ≤ i ≤ m ). A processor can process a task of size less than or equal to its capacity in 1 second, but it cannot execute processes whose size is greater than its capacity.
A processor can execute multiple processes one after the other, but needs to pause for 1 second after completing its current one. Multiple processors can work on different processes simultaneously.
Find the minimum time to execute all the processes or return -1 if there is no way to execute all the processes.

Example
It is given that n = 3, processSize = [2, 5, 3], m = 3 and capacity = [6, 2, 4]
The optimal way to assign processes is to give:

The first processor the second process
The second processor the first process
The third processor the third process
All of them complete their processes in 1 second. Therefore, the minimum time required is 1 second.

Sample Case 0:
Sample Input:
STDIN FUNCTION
5 processSize[] size n = 5
1 processSize = [1, 2, 3, 4, 6]
3 capacity[] size n = 3
4 capacity = [4, 1, 4]
6
Sample Output: 3
Explanation: Assign the second and third process to the first processor. It completes the first process in 1 second, then pauses for another second before completing the third process in 1 second

Sample Case 1:
Sample Input:
STDIN FUNCTION
3 processSize[] size n = 3
2 processSize = [2, 5, 8]
5 capacity[] size n = 3
8 capacity = [6, 7, 4]
3
6
7
4
Sample Output: -1
Explanation: No processor has the required capacity to process the third process (size = 8), so there is no way to process them all.
"""

def minExecutionTime(processSize, capacity):
    processSize.sort(reverse=True)
    capacity.sort(reverse=True)

    if processSize[0] > capacity[0]:
        return -1

    time = 0
    i = 0  # pointer for processSize

    while i < len(processSize):
        j = 0  # pointer for capacity
        count = 0

        # Try to assign up to len(capacity) tasks this round
        while i < len(processSize) and j < len(capacity):
            if capacity[j] >= processSize[i]:
                i += 1
                count += 1
            j += 1

        time += 2  # 1s processing + 1s pause

    return time - 1  # no pause after final round
