# TODO: TLE. sigh.
from typing import Optional


class Solution:
    def dummy(*_: object) -> None: ...


class SeatManager:
    def __init__(self, n: int):
        self.reserved = [False for _ in range(n+1)]
        self.unreserved_index = 0

    def reserve(self) -> int:
        self.reserved[self.unreserved_index] = True
        seatNumber = self.unreserved_index + 1

        new_index = self.unreserved_index + 1
        while self.reserved[new_index]:
            new_index += 1

        self.unreserved_index = new_index

        return seatNumber

    def unreserve(self, seatNumber: int) -> None:
        index = seatNumber - 1
        self.reserved[index] = False
        if index < self.unreserved_index:
            self.unreserved_index = index


tests = [
    (
        (["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"],
         [[5], [], [], [2], [], [], [], [], [5]],
         ),
        [None, 1, 2, None, 2, 3, 4, 5, None],
    ),
    (
        (["SeatManager", "reserve", "unreserve", "reserve", "unreserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "reserve", "unreserve", "unreserve", "unreserve", "reserve", "unreserve", "reserve", "reserve", "unreserve", "unreserve", "reserve", "unreserve", "unreserve", "unreserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve"],
         [[798], [], [1], [], [1], [], [1], [], [], [], [], [], [5], [3], [2], [], [4], [
         ], [], [1], [3], [], [2], [4], [1], [], [1], [], [], [], [], [1], [], [], []],
         ),
        [None, 1, None, 1, None, 1, None, 1, 2, 3, 4, 5, None, None, None, 2, None,
            3, 4, None, None, 1, None, None, None, 1, None, 1, 2, 3, 4, None, 1, 5, 6],
    ),

]


def validator(
        _: object,
        inputs: tuple[list[str], list[list[int]]],
        expected: list[Optional[int]]
) -> None:
    obj = SeatManager(0)
    method = zip(*inputs)
    for (method_name, args), expected_val in zip(method, expected):
        if method_name == "SeatManager":
            obj = SeatManager(*args)
            continue

        retval = getattr(obj, method_name)(*args)
        assert retval == expected_val, (retval, expected_val)
