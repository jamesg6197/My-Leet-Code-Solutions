def coinChange(self, coins: List[int], amount: int) -> int:
        DP = {}
        DP[0] = 0
        for i in range(1, amount + 1):
            DP[i] = amount + 1
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    DP[i] = min(1 + DP[i - coin], DP[i])
        if DP[amount] == amount + 1:
            return -1
        return DP[amount]
