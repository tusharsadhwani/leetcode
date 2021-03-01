class Solution:
    def hammingWeight(self, n: int) -> int:
        if n < 0:
            n = 2 ** 32 + n

        binary = f'{n:0>32b}'
        return binary.count('1')


tests = [
    (
        (11,),
        3,
    ),
    (
        (128,),
        1,
    ),
    (
        (-3,),
        31,
    ),
]
