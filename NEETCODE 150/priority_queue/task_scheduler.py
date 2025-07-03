"""
621. Task Scheduler
 Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.
https://leetcode.com/problems/task-scheduler/description/
Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.
"""
class Solution:
    # Time Complexity:
    #   Best, Average, Worst case: O(n), where n is the total number of tasks
    # Space Complexity: O(1) (bounded heap size due to 26 max task types)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count frequency of each task
        count = Counter(tasks)

        # Step 2: Max-heap to always process the most frequent task first
        # We negate counts to use Python's min-heap as a max-heap
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0  # Total time units needed to finish all tasks
        q = deque()  # Queue to keep track of tasks in cooldown: [remaining_count, cooldown_expiry_time]

        # Step 3: Simulate each unit of time
        while maxHeap or q:
            time += 1

            # If there are tasks ready to be processed
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)  # Pop the most frequent task (add 1 to remove one execution as its max heap)
                # If task still has remaining executions, add it to cooldown queue
                if cnt:
                    q.append([cnt, time + n])  # Task can be scheduled again after 'n' units

            # If a task's cooldown is over, push it back into the heap
            if q and q[0][1] == time:
                cnt = q.popleft()[0]
                heapq.heappush(maxHeap, cnt)

        return time  # Total time to finish all tasks with cooling periods
