"""
@author: xiongbiao
@date: 2022-02-24 23:47
"""

# 2 * -5
# 2 * -17
# 6 - 20
# 10 * 5
# -2 * 5

class Solution:
    def diffWaysToCompute(self, expression: str):
        return self.extract(expression)

    def extract(self, exp):
        if '+' not in exp and '*' not in exp and '-' not in exp:
            return [int(exp)]
        sub = []
        for i, e in enumerate(exp):
            if e in '+-*':
                l = self.extract(exp[:i])
                r = self.extract(exp[i+1:])
                for i in l:
                    for j in r:
                        if e == '+':
                            sub.append(i + j)
                        elif e == '-':
                            sub.append(i - j)
                        else:
                            sub.append(i * j)
        return sub

print(Solution().diffWaysToCompute('100-12*9'))

