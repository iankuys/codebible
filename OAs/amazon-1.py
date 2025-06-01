# LeetCode Problem 1: https://leetcode.com/problems/
from math import ceil
from tracemalloc import take_snapshot


def findTotalExecutionTime(execution):
    task_queue = {}
    time_elapsed = 0
    for process in execution:
        if process not in task_queue:
            task_queue[process] = process
            time_elapsed = time_elapsed + process
        else:
            task_queue[process] = ceil(task_queue[process]/2)
            time_elapsed = time_elapsed + task_queue[process]
            
    return time_elapsed

arr = [5,5,3,6,5,3]
print(findTotalExecutionTime(arr))
