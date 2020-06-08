## written by xiongbiao
## date 2020-6-7
'''
假设你有一个特殊的键盘包含下面的按键：
Key 1: (A)：在屏幕上打印一个 'A'。
Key 2: (Ctrl-A)：选中整个屏幕。
Key 3: (Ctrl-C)：复制选中区域到缓冲区。
Key 4: (Ctrl-V)：将缓冲区内容输出到上次输入的结束位置，并显示在屏幕上。
现在，你只可以按键 N 次（使用上述四种按键），请问屏幕上最多可以显示几个 'A'呢？
'''
class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [0] * (N + 1)
        for i in range(1, N+1):
            dp[i] = dp[i-1] + 1
            for j in range(0, i-1):
                dp[i] = max(dp[i], dp[j] * (i - j - 1))
        return dp[-1]
Solution().maxA(8)

