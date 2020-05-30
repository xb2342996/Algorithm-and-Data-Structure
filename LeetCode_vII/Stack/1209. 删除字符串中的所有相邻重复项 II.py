## written by xiongbiao
## date 2020-5-30
'''
给你一个字符串 s，「k 倍重复项删除操作」将会从 s 中选择 k 个相邻且相等的字母，并删除它们，使被删去的字符串的左侧和右侧连在一起。
你需要对 s 重复进行无限次这样的删除操作，直到无法继续为止。
在执行完所有删除操作后，返回最终得到的字符串。
'''
class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []

        for w in s:
            if stack and w == stack[-1][0]:
                if stack[-1][1] == k-1:
                    stack.pop()
                else:
                    elem, cnt = stack.pop()
                    stack.append((elem, cnt + 1))
            else:
                stack.append((w, 1))

        s = ''
        for e, c in stack:
            s += e * c
        return s

Solution().removeDuplicates('abcd', 2)