## written by xiongbiao
## date 2020-10-17

'''
给定字符串列表，你需要从它们中找出最长的特殊序列。最长特殊序列定义如下：该序列为某字符串独有的最长子序列（即不能是其他字符串的子序列）。
子序列可以通过删去字符串中的某些字符实现，但不能改变剩余字符的相对顺序。空序列为所有字符串的子序列，任何字符串为其自身的子序列。
输入将是一个字符串列表，输出是最长特殊序列的长度。如果最长特殊序列不存在，返回 -1 。
'''

class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        length = len(strs)
        max_length = -1
        for i in range(0, length):
            j = 0
            while j < length:
                if i == j:
                    j += 1
                    continue
                if self.isSubSeq(strs[i], strs[j]):
                    break
                j += 1
            if j == length:
                max_length = max(max_length, len(strs[i]))
        return max_length

    def isSubSeq(self, str1, str2):
        j = 0
        for i, s in enumerate(str2):
            if str1[j] == s:
                j += 1
            if j == len(str1):
                break
        return j == len(str1)

# print(Solution().isSubSeq("c", "c"))
print(Solution().findLUSlength(["a", "a", "a"]))