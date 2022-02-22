"""
@author: xiongbiao
@date: 2022-02-22 23:51
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        length = len(s)
        half = length // 2
        for i in range(half):
            s[i], s[length-i-1] = s[length-i-1], s[i]

        # print(s)
        start, end = 0, 0
        while end < length:
            if s[end] == ' ':
                self.reverse_word(s, start, end)
                start = end + 1
            end += 1
        self.reverse_word(s, start, end)
        print(s)

    def reverse_word(self,s, start, end):
        word_size = end - start
        half = word_size // 2
        for i in range(start, start + half):
            s[i], s[end - i - 1 + start] = s[end - i - 1 + start], s[i]

Solution().reverseWords(['a', ' ', 'b', 'c', ' ', 'x', 'y', 'z'])