class Solution:
    def threeSum(self, nums: list[int]) -> list[tuple[int, int, int]]:
        counter: dict[int, int] = {}
        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1

        def is_valid(a: int, b: int, c: int) -> bool:
            if a == c:
                return counter[a] >= 3
            if a == b:
                return counter[a] >= 2
            if b == c:
                return counter[b] >= 2
            return True

        unique_sorted = sorted(counter.keys())
        length = len(unique_sorted)
        result: list[tuple[int, int, int]] = []
        for i in range(length):
            ni = unique_sorted[i]
            if ni > 0:  # optional; optimized for early return
                break
            for j in range(i, length):
                nj = unique_sorted[j]  # implies ni <= nj
                nk = 0 - ni - nj
                if nj > nk:  # requires nj <= nk
                    break  # optional; optimized for early return
                if nk in counter and is_valid(ni, nj, nk):
                    result.append((ni, nj, nk))
        return result


tests = [
    (
        ([-1, 0, 1, 2, -1, -4],),
        [(-1, -1, 2), (-1, 0, 1)],
    ),
    (
        ([],),
        [],
    ),
    (
        ([0],),
        [],
    ),
]
