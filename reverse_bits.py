class Solution:
    def reverseBits(self, n: int) -> int:
        if n < 0:
            n = 2 ** 32 + n

        binary = f'{n:0>32b}'
        reversed_binary = binary[::-1]
        return int(reversed_binary, base=2)


tests = [
    (
        (43261596,),
        964176192,
    ),
    (
        (-3,),
        3221225471,
    ),
]
