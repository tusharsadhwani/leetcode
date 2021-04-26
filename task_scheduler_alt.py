from collections import Counter


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counters = list(Counter(tasks).values())
        counters.sort()
        max_freq = counters.pop()
        max_idle_time = (max_freq - 1) * n

        idle_time = max_idle_time
        while counters and idle_time > 0:
            idle_time -= min(max_freq - 1, counters.pop())

        if idle_time < 0:
            idle_time = 0

        return len(tasks) + idle_time


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
