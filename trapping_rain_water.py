class Solution:
    def trap(self, heights: list[int]) -> int:
        highest_pillar, highest_index = 0, 0
        for index, height in enumerate(heights):
            if height > highest_pillar:
                highest_pillar = height
                highest_index = index

        left, right = heights[:highest_index], heights[highest_index:]

        trapped_water = 0

        highest_left = 0
        for height in left:
            highest_left = max(highest_left, height)

            water_height = highest_left - height
            trapped_water += water_height

        highest_right = 0
        for height in reversed(right):
            highest_right = max(highest_right, height)

            water_height = highest_right - height
            trapped_water += water_height

        return trapped_water


tests = [
    (
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],),
        6,
    ),
    (
        ([4, 2, 0, 3, 2, 5],),
        9,
    ),
]
