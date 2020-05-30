## written by xiongbiao
## date 2020-5-30
'''
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
'''

class Solution(object):
    '''
    压栈出栈
    '''
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        stack = []
        num, word = 0, ''
        while len(s) > 0:
            c = s.pop(0)
            if c.isdigit():
                num = num * 10 + int(c)
            elif c.isalpha():
                word += c
            elif c == '[':
                stack.append((word, num))
                word, num = '', 0
            else:
                w, n = stack.pop()
                word = w + word * n

        return word


Solution().decodeString('3[a2[c]]')