from collections import defaultdict
from heapq import heappop, heappush


###############################################################
## NOTE: Sigh.                                               ##
## I Wrote an O(n^2) solution without thinking about it.     ##
## You don't need to start counting from 0 for every number. ##
## Improved version in alt.                                  ##
###############################################################

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        gap = n + 1
        heap: list[tuple[int, str]] = []
        task_times: defaultdict[str, int] = defaultdict(int)
        largest_time = 0

        for _, task in enumerate(tasks):
            next_task_time = task_times[task]
            heappush(heap, (next_task_time, task))
            largest_time = max(largest_time, next_task_time)
            task_times[task] = next_task_time + gap

        time_slots = [''] * largest_time
        while heap:
            min_time, task = heappop(heap)
            current_time = min_time

            while True:
                if current_time >= len(time_slots):
                    time_slots.append(task)
                    break

                if time_slots[current_time] == '':
                    time_slots[current_time] = task
                    break

                current_time += 1

        return len(time_slots)


tests = [
    (
        (["A", "A", "A", "B", "B", "B"], 2,),
        8,
    ),
    (
        (["A", "A", "A", "B", "B", "B"], 0,),
        6,
    ),
    (
        (["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2,),
        16,
    ),
]
