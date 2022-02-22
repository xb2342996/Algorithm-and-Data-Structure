"""
@author: xiongbiao
@date: 2021-05-20 23:43
"""
'''
牌组中的每张卡牌都对应有一个唯一的整数。你可以按你想要的顺序对这套卡片进行排序。
最初，这些卡牌在牌组里是正面朝下的（即，未显示状态）。
现在，重复执行以下步骤，直到显示所有卡牌为止：
从牌组顶部抽一张牌，显示它，然后将其从牌组中移出。
如果牌组中仍有牌，则将下一张处于牌组顶部的牌放在牌组的底部。
如果仍有未显示的牌，那么返回步骤 1。否则，停止行动。
返回能以递增顺序显示卡牌的牌组顺序。
答案中的第一张牌被认为处于牌堆顶部。
'''

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()

        if len(deck) == 1:
            return deck
        last = deck.pop(-1)
        queue = [last]
        while len(deck) > 0:
            card = deck.pop(-1)
            top = queue.pop(-1)
            queue.insert(0, top)
            queue.insert(0, card)
        return queue


print(Solution().deckRevealedIncreasing([17,13,11,2,3,5,7]))