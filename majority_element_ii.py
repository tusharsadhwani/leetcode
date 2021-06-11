class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        candidate1, candidate2 = 0, 0
        count1, count2 = 0, 0

        for num in nums:
            if candidate1 == num:
                count1 += 1
                continue

            if candidate2 == num:
                count2 += 1
                continue

            # NOTE: count checks must come AFTER candidate == num checks
            if count1 == 0:
                candidate1 = num
                count1 += 1
                continue

            if count2 == 0:
                candidate2 = num
                count2 += 1
                continue

            # If we have reached this point,
            # we have found 3 different items, which we can count out.
            count1 -= 1
            count2 -= 1

        result = set()
        for candidate in (candidate1, candidate2):
            if nums.count(candidate) > len(nums) // 3:
                result.add(candidate)

        return list(result)


tests = [
    (
        ([3, 2, 3],),
        [3],
    ),
    (
        ([1],),
        [1],
    ),
    (
        ([1, 2],),
        [1, 2],
    ),
    (
        ([2, 2],),
        [2],
    ),
    (
        ([2, 1, 1, 3, 1, 4, 5, 6],),
        [1],
    ),
]
