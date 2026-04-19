class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        coins
        1 dolalr 5 dollar
        return # of disntcit combinations that total up to amoutn
        disitncit combinations

        unlimtied eqach coin
        can reuse
        kanpsap take it o rnot 
        """
        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1): ## forwards here so can reuse coins
            ## but we iterating items -> amount to make sure discintinc combos
            ## can never use another coin again in the later
                dp[i] += dp[i-coin]
        return dp[amount]