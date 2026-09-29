class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[-1] * n for _ in range(n)]
        def solve(i, j):
            if j - i < 2:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            ans = float('inf')
            for k in range(i + 1, j):
                triangle = values[i] * values[k] * values[j]
                left = solve(i, k)
                right = solve(k, j)
                total = left + triangle + right
                if total < ans:
                    ans = total
            dp[i][j] = ans
            return ans
        return solve(0, n - 1)