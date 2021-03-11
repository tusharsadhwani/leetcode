class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""
        longest_length = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                length = j+1-i
                if length < longest_length:  # optimization
                    continue
                substr = s[i:j+1]
                if substr == substr[::-1] and len(substr) > len(longest_palindrome):
                    longest_palindrome = substr
                    longest_length = length

        return longest_palindrome


tests = [
    (
        ("babad",),
        "bab",
    ),
    (
        ("cbbd",),
        "bb",
    ),
    (
        ("a",),
        "a",
    ),
    (
        ("ac",),
        "a",
    ),

]
