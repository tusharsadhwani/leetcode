class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x < 0:
            x = 2 ** 32 + x
        if y < 0:
            n = 2 ** 32 + y

        binary_x = f'{x:0>32b}'
        binary_y = f'{y:0>32b}'
        distance = 0
        for bit_x, bit_y in zip(binary_x, binary_y):
            if bit_x != bit_y:
                distance += 1

        return distance


tests = [
    (
        (1, 4,),
        2,
    ),
]
