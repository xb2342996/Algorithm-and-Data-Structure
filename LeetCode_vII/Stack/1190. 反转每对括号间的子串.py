## written by xiongbiao
## date 2020-5-30
'''
给出一个字符串 s（仅含有小写英文字母和括号）。
请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。
'''
class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        def helper(s):
            w = ''
            while len(s) > 0:
                c = s.pop(0)
                if c == '(':
                    o = helper(s)
                    w += o[::-1]
                elif c.isalpha():
                    w += c
                elif c == ')':
                    break
            return w
        return helper(list(s))

Solution().reverseParentheses('a(bcdefghijkl(mno)p)q')
