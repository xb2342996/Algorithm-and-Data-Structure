## written by xiongbiao
## date 2020-5-30
'''
编写一个 StockSpanner 类，它收集某些股票的每日报价，并返回该股票当日价格的跨度。
今天股票价格的跨度被定义为股票价格小于或等于今天价格的最大连续日数（从今天开始往回数，包括今天）。
'''


class StockSpanner(object):

    def __init__(self):
        self.prices = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        weight = 1
        while self.prices and self.prices[-1][0] < price:
            weight += self.prices.pop()[1]
        self.prices.append((price, weight))
        return weight
S = StockSpanner()
print(S.next(100))
print(S.next(80))
print(S.next(60))
print(S.next(70))
print(S.next(60))
print(S.next(75))
print(S.next(85))
