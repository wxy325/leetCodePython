__author__ = 'wxy325'
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):

        index = 0
        total = 0
        while index < len(prices) - 1:
            if prices[index] >= prices[index + 1]:
                index += 1
                continue
            else:
                rIndex = index + 1
                while rIndex < len(prices) - 1:
                    if prices[rIndex] > prices[rIndex + 1]:
                        break
                    rIndex += 1
                total += (prices[rIndex] - prices[index])
                index = rIndex + 1
        return total





if __name__ == '__main__':
    s = Solution()
    assert s.maxProfit([1, 3, 2, 4]) == 4
    assert s.maxProfit([1, 2, 3, 2, 4]) == 4
    assert s.maxProfit([3, 2, 1, 4, 5]) == 4
    assert s.maxProfit([4, 3, 2, 1]) == 0