class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        # Idea: keep two reversed pointers, for odd and even anomalies,
        # and scan array until we have looked at all possible mismatched
        # parity pairs.
        start = 0
        odd_anomaly = even_anomaly = len(nums) - 1
        if odd_anomaly % 2 == 0:
            odd_anomaly -= 1
        if even_anomaly % 2 != 0:
            even_anomaly -= 1

        while start < odd_anomaly or start < even_anomaly:
            while start < odd_anomaly or start < even_anomaly:
                num1 = nums[start]
                is_wrong_parity = num1 % 2 != start % 2
                if is_wrong_parity:
                    break

                start += 1
            else:
                # No anomalies found
                break

            if num1 % 2 == 0:
                while start < even_anomaly:
                    num2 = nums[even_anomaly]
                    is_opposite_parity = num2 % 2 != even_anomaly % 2
                    if is_opposite_parity:
                        break

                    even_anomaly -= 2

                nums[start], nums[even_anomaly] = nums[even_anomaly], nums[start]

            else:
                while start < odd_anomaly:
                    num2 = nums[odd_anomaly]
                    is_opposite_parity = num2 % 2 != odd_anomaly % 2
                    if is_opposite_parity:
                        break

                    odd_anomaly -= 2

                nums[start], nums[odd_anomaly] = nums[odd_anomaly], nums[start]

        return nums


tests = [
    (
        ([4, 2, 5, 7],),
        [4, 5, 2, 7],
    ),
    (
        ([2, 3],),
        [2, 3],
    ),
    (
        ([2, 3, 1, 1, 4, 0, 0, 4, 3, 3],),
        [2, 3, 4, 1, 4, 3, 0, 1, 0, 3],
    ),

]
