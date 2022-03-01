"""
@author: xiongbiao
@date: 2022-02-27 22:47
"""

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.no_edge_map = {
            '0': '0'
        }
        self.center_map = {
            '1': '1',
            '8': '8'
        }
        self.sym_map = {
            '6': '9',
            '9': '6'
        }
        self.ans = []
        z = {**self.center_map, **self.no_edge_map}
        if n == 1:
            return list(z.values())
        index = n // 2 - 1
        print(index)
        if n % 2 == 1:
            for s in z.keys():
                self.make(index, s)
        else:
            self.make(index, '')

        return self.ans


    def make(self, index, digit):
        z = {**self.center_map, **self.sym_map}
        if index == 0:
            for k, v in z.items():
                new_digit = k + digit + v
                self.ans.append(new_digit)
            return
        z = {**z, **self.no_edge_map}
        for s in z:
            self.make(index-1, s + digit + z[s])

print(Solution().findStrobogrammatic(4))