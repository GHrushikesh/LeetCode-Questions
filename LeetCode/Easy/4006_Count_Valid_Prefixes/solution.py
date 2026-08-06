class Solution:
    def countValidPrefixes(self, s: str) -> int:
        ans = 0
        zero = 0
        one = 0
        for c in s:
            if c == '0':
                zero += 1
            else:
                one += 1
            if abs(zero - one) <= 1:
                ans += 1
        return ans