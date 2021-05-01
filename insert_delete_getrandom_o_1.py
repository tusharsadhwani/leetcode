from typing import Union
import random


class Solution:
    def dummy(*_: object) -> None: ...


class RandomizedSet:
    def __init__(self) -> None:
        self.set: set[int] = set()

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False

        self.set.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.set:
            self.set.remove(val)
            return True

        return False

    def getRandom(self) -> int:
        # # simulated randomness, sadly python sets are ordered now
        # for _ in range(random.randint(0, 10)):
        self.set.add(self.set.pop())

        val = self.set.pop()
        self.set.add(val)
        return val


tests = [
    (
        (
            ["insert",
             "remove",
             "insert",
             "getRandom",
             "remove",
             "insert",
             "getRandom"],
            [[1], [2], [2], [], [1], [2], []],
        ),
        [True, False, True, 2, True, False, 2],
    ),
]


def validator(
        _: object,
        inputs: tuple[list[str], list[list[int]]],
        expected: list[Union[bool, int, None]]
) -> None:
    obj = RandomizedSet()
    method = zip(*inputs)
    for (method_name, args), expected_val in zip(method, expected):
        retval = getattr(obj, method_name)(*args)
        assert retval == expected_val, (retval, expected_val)
