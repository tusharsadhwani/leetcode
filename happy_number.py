class Solution:
    def isHappy(self, n: int) -> bool:
        seen: set[int] = set()
        while True:
            total = 0
            while n > 0:
                last_digit = n % 10
                n //= 10
                total += last_digit ** 2

            if total == 1:
                return True

            if total in seen:
                return False

            seen.add(total)
            n = total


tests = [
    (
        (19,),
        True,
    ),
    (
        (2,),
        False,
    ),
]
