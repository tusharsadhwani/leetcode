def iterate(
        text: str,
        forward_index: int,
        reverse_index: int) -> tuple[int, int]:
    """Finds the indices of the next set of valid alphabets in the string."""
    while 0 <= forward_index < len(text) and not text[forward_index].isalnum():
        forward_index += 1
    while 0 <= reverse_index < len(text) and not text[reverse_index].isalnum():
        reverse_index -= 1

    return forward_index, reverse_index


class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = s.lower()
        front, back = 0, len(text) - 1
        is_palindrome = True
        while front < back:
            front, back = iterate(text, front, back)

            if (front < 0 or front >= len(text) or
                    back < 0 or back >= len(text)):
                break

            if text[front] != text[back]:
                is_palindrome = False
                break

            front += 1
            back -= 1

        return is_palindrome


tests = [
    (
        ("A man, a plan, a canal: Panama",),
        True,
    ),
    (
        ("race a car",),
        False,
    ),
]
