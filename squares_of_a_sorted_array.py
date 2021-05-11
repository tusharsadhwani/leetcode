import sys


def merge(list1: list[int], list2: list[int]) -> list[int]:
    output: list[int] = []
    index1, index2 = 0, 0
    while index1 < len(list1) and index2 < len(list2):
        num1, num2 = list1[index1], list2[index2]
        if num1 < num2:
            output.append(num1)
            index1 += 1
        else:
            output.append(num2)
            index2 += 1

    output += list1[index1:]
    output += list2[index2:]
    return output


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        positive_start = sys.maxsize
        for index, num in enumerate(nums):
            if num >= 0:
                positive_start = index
                break

        negatives, positives = nums[:positive_start], nums[positive_start:]

        positive_squares = [num ** 2 for num in positives]
        negative_squares = [num ** 2 for num in reversed(negatives)]

        return merge(positive_squares, negative_squares)


tests = [
    (
        ([-4, -1, 0, 3, 10],),
        [0, 1, 9, 16, 100],
    ),
    (
        ([-7, -3, 2, 3, 11],),
        [4, 9, 9, 49, 121],
    ),
]
