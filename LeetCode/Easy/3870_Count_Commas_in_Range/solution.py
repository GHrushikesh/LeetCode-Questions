class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0 
        for i in range(1000, n + 1):
            ans += 1
        return ans