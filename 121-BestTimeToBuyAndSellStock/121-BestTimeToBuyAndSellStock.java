// Last updated: 8/16/2026, 9:52:23 PM
class Solution {
    public int maxProfit(int[] prices) {
        // // brute force
        // int res = 0;
        // int n = prices.length;
        // for(int i = 0; i < n - 1; i ++) {
        //     int buy = prices[i];
        //     for(int j = i + 1; j < n; j ++) {
        //         int sell = prices[j];
        //         if(sell - buy > res) {
        //             res = sell - buy;
        //         }
        //     }
        // }
        // return res;

        // current profit = current price - previous min price
        int res = 0, n = prices.length;
        int minPrice = Integer.MAX_VALUE;
        for(int i = 0; i < n; i++) {
            if(prices[i] < minPrice) {
                minPrice = prices[i];
            }
            if(prices[i] - minPrice > res) {
                res = prices[i] - minPrice;
            }
        }
        return res;
    }
}