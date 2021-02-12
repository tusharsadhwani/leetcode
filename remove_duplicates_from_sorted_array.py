class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        offset = 0
        values: set[int] = set()
        for index, num in enumerate(nums):
            nums[index - offset] = num

            if num in values:
                offset += 1
            else:
                values.add(num)

        new_length = len(nums) - offset
        return new_length


tests = [
    (
        ([1, 1, 2],),
        (2, [1, 2]),
    ),
    (
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4],),
        (5, [0, 1, 2, 3, 4]),
    ),
]


def validator(removeDuplicates, inputs, outputs):
    nums, = inputs
    length, expected = outputs

    new_length = removeDuplicates(nums)

    assert length == new_length, (length, new_length)
    assert nums[:new_length] == expected, (nums[:new_length], expected)
