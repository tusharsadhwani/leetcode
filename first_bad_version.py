from typing import Callable


def isBadVersion(i: int) -> bool: ...


class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 1, n
        bad_index = -1

        while start <= end:
            mid = (start + end) // 2
            bad = isBadVersion(mid)
            if bad:
                bad_index = mid if bad_index == -1 else min(bad_index, mid)
                end = mid - 1
            else:
                start = mid + 1

        return bad_index


tests = [
    (
        (5, 4,),
        4,
    ),
    (
        (1, 1,),
        1,
    ),
]


def validator(
        firstBadVersion: Callable[[int], int],
        inputs: tuple[int, int],
        expected: int,
) -> None:
    n, bad = inputs
    globals()['isBadVersion'] = lambda i: i >= bad
    output = firstBadVersion(n)
    assert output == expected, (output, expected)
