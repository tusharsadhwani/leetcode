class Solution:
    def countAndSay(self, n: int) -> str:
        spoken_string = "1"

        for _ in range(1, n):
            current_digit = ""
            current_count = 0

            new_spoken_string = ""
            for digit in spoken_string:
                if digit == current_digit:
                    current_count += 1
                else:
                    if current_digit:
                        new_spoken_string += f'{current_count}{current_digit}'

                    current_digit = digit
                    current_count = 1

            new_spoken_string += f'{current_count}{current_digit}'
            spoken_string = new_spoken_string
        return spoken_string


tests = [
    (
        (1,),
        "1",
    ),
    (
        (4,),
        "1211",
    ),
]
