class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        strings: list[str] = []
        for i in range(1, n+1):
            string = ''
            if i % 3 == 0:
                string += 'Fizz'
            if i % 5 == 0:
                string += 'Buzz'
            strings.append(string or str(i))

        return strings


tests = [
    (
        (15,),
        [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz",
        ],
    ),
]
