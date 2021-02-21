"""
@author: xiongbiao
@date: 2021-02-21 21:50
"""
'''
给定一个字符串 ring，表示刻在外环上的编码；给定另一个字符串 key，表示需要拼写的关键词。您需要算出能够拼写关键词中所有字符的最少步数。
最初，ring 的第一个字符与12:00方向对齐。您需要顺时针或逆时针旋转 ring 以使 key 的一个字符在 12:00 方向对齐，然后按下中心按钮，以此逐个拼写完 key 中的所有字符。
旋转 ring 拼出 key 字符 key[i] 的阶段中：
您可以将 ring 顺时针或逆时针旋转一个位置，计为1步。旋转的最终目的是将字符串 ring 的一个字符与 12:00 方向对齐，并且这个字符必须等于字符 key[i] 。
如果字符 key[i] 已经对齐到12:00方向，您需要按下中心按钮进行拼写，这也将算作 1 步。按完之后，您可以开始拼写 key 的下一个字符（下一阶段）, 直至完成所有拼写。
'''
class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        from collections import defaultdict
        len_ring = len(ring)
        len_key = len(key)
        dp = [[float('inf')] * len_ring for _ in range(len_key)]
        word = defaultdict(list)
        for i, r in enumerate(ring):
            word[r].append(i)

        print(word)
        for i in word[key[0]]:
            dp[0][i] = min(i, len_ring-i) + 1

        for i in range(1, len_key):
            for j in word[key[i]]:
                for k in word[key[i-1]]:
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + min(abs(j - k), len_ring - abs(j - k)) + 1)
        print(dp)
        return min(dp[len_key-1])

print(Solution().findRotateSteps("edcba", "abcde"))