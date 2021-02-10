class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        end = len(s) - 1
        for index in range(len(s)//2):
            s[index], s[end-index] = s[end-index], s[index]
