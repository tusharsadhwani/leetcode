class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()

        new_intervals: list[list[int]] = []

        prev_interval = intervals[0]
        for index in range(1, len(intervals)):
            interval = intervals[index]

            if interval[0] > prev_interval[1]:
                new_intervals.append(prev_interval)
                prev_interval = interval
            else:
                prev_interval = [
                    min(prev_interval[0], interval[0]),
                    max(prev_interval[1], interval[1]),
                ]

        new_intervals.append(prev_interval)

        return new_intervals


tests = [
    (
        ([[1, 3], [2, 6], [8, 10], [15, 18]],),
        [[1, 6], [8, 10], [15, 18]],
    ),
    (
        ([[1, 4], [4, 5]],),
        [[1, 5]],
    ),
]
