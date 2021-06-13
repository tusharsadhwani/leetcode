# NOTE: Greedy doesn't work, see the last test case.
class Solution:
    def maxScore(self, card_points: list[int], k: int) -> int:
        initial_values = card_points[-k:]
        current_total = max_total = sum(initial_values)

        for index in range(k):
            new_card = card_points[index]
            leftmost_previous_card = card_points[index-k]

            current_total += new_card
            current_total -= leftmost_previous_card

            max_total = max(max_total, current_total)

        return max_total


tests = [
    (
        ([1, 2, 3, 4, 5, 6, 1], 3),
        12,
    ),
    (
        ([2, 2, 2], 2,),
        4,
    ),
    (
        ([9, 7, 7, 9, 7, 7, 9], 7,),
        55,
    ),
    (
        ([1, 1000, 1], 1,),
        1,
    ),
    (
        ([1, 79, 80, 1, 1, 1, 200, 1], 3,),
        202,
    ),
    (
        ([11, 49, 100, 20, 86, 29, 72], 4,),
        232,
    ),
]
