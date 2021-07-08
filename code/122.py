# 给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。

# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 贪心，上涨卖，下降不卖，最近两个交易日
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        money = 0
        for i in range(1,len(prices)):
            if prices[i-1] < prices[i]:
                money = money + prices[i] - prices[i-1]
        return money
