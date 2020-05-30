## written by xiongbiao
## date 2020-5-29

'''
给定一个化学式formula（作为字符串），返回每种原子的数量。
原子总是以一个大写字母开始，接着跟随0个或任意个小写字母，表示原子的名字。
如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。例如，H2O 和 H2O2 是可行的，但 H1O2 这个表达是不可行的。
两个化学式连在一起是新的化学式。例如 H2O2He3Mg4 也是化学式。
一个括号中的化学式和数字（可选择性添加）也是化学式。例如 (H2O2) 和 (H2O2)3 是化学式。
给定一个化学式，输出所有原子的数量。格式为：第一个（按字典序）原子的名子，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。
'''

class Solution(object):
    '''
    编写一个方法 parse 来解析化学式，返回一个由原子名称映射到原子个数的哈希表 count。
    将把 i 设为全局变量：在调用 parse 函数中递增 i。
    当遇到 '('，则解析括号内的内容（直到括号结束），并将其添加到计数中。
    否则，则应该遇到一个大写字符：我们将解析其余的字母以获得名称，并在哈希表中添加该字符（若表中存在则增加计数）。
    最终，我们将乘以括号系数以得到最终结果。
    '''
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        def helper(f):
            elem = ''
            elements = {}
            elem_dict = {}
            nums = 0
            while len(f) > 0:
                s = f.pop(0)
                if 65 <= ord(s) < 91 or s == '(':
                    elements = self.add_element(elem, elem_dict, elements, nums)
                    nums = 0
                    if s == '(':
                        elem = ''
                        elem_dict = helper(f)
                    else:
                        elem = s
                elif 97 <= ord(s) < 128:
                    elem += s
                elif s.isdigit():
                    nums = 10 * nums + int(s)
                elif s == ')':
                    break
            elements = self.add_element(elem, elem_dict, elements, nums)

            return elements

        dicts = helper(list(formula))
        for k, v in dicts.items():
            print(k, v)
        ans = sorted(dicts.items())
        s = ''
        for e, n in ans:
            if n != 1:
                s += e + str(n)
            else:
                s += e
        return s

    def add_element(self, elem, elem_dict, elements, nums):
        nums = 1 if nums == 0 else nums
        if elem != '':
            if elem in elements:
                elements[elem] += nums
            else:
                elements[elem] = nums
        if len(elem_dict) > 0:
            for k, v in elem_dict.items():
                if k in elements:
                    elements[k] += nums * v
                else:
                    elements[k] = nums * v
        return elements
print(Solution().countOfAtoms('K4(ON(SO3)2)2'))