class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let max = 0;
        let buy = Infinity;

        for (let i = 0; i < prices.length; i++) {
            if (prices[i] - buy < 0) {
                buy = prices[i];
            }
            else {
                max = Math.max(max, prices[i]- buy);
            }
        }
        return max;
    }
}
