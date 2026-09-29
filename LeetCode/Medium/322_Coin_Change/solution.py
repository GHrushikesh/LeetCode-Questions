class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    previous = dp[i - coin]
                    current = previous + 1
                    if current < dp[i]:
                        dp[i] = current
        if dp[amount] == amount + 1:
            return -1
        return dp[amount]