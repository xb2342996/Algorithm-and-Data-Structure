# written by xiongbiao
# date 2020-11-22

'''
在LeetCode商店中， 有许多在售的物品。
然而，也有一些大礼包，每个大礼包以优惠的价格捆绑销售一组物品。
现给定每个物品的价格，每个大礼包包含物品的清单，以及待购物品清单。请输出确切完成待购清单的最低花费。
每个大礼包的由一个数组中的一组数据描述，最后一个数字代表大礼包的价格，其他数字分别表示内含的其他种类物品的数量。
任意大礼包可无限次购买。
'''
class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        def dfs(needs):
            res = sum([needs[i] * price[i] for i in range(len(needs))])
            for s in special:
                updated_needs = [needs[i] - s[i] for i in range(len(needs))]
                if min(updated_needs) >= 0:
                    res = min(res, dfs(tuple(updated_needs)) + s[-1])

            return res

        return dfs(tuple(needs))

print(Solution().shoppingOffers([0,0,0],[[1,1,0,4],[2,2,1,9]],[1,1,1]))