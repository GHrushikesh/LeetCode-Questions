class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""

        for ch in s:
            if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or ('0' <= ch <= '9'):
                new += ch.lower()

        return new == new[::-1]