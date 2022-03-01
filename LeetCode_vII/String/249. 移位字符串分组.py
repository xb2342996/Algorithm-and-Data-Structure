"""
@author: xiongbiao
@date: 2022-02-28 22:41
"""

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        # from collections import defaultdict
        # map = defaultdict(int)
        # valid = defaultdict(bool)
        # for string in strings:
        #     map[string] += 1
        #     valid[string] = False
        # ans = []
        # for string in strings:
        #     if not valid[string]:
        #         group = []
        #         for i in range(26):
        #             w = ''
        #             for s in string:
        #                 asc = (ord(s) + i - 97) % 26 + 97
        #                 w += chr(asc)
        #             if w in valid.keys():
        #                 for i in range(map[w]):
        #                     group.append(w)
        #                 valid[w] = True
        #         ans.append(group)
        # return ans
        from collections import defaultdict
        def count_hash(s):
            values = []
            if len(s) >= 1:
                for i in range(len(s) - 1):
                    d = (ord(s[i+1]) - ord(s[i])) % 26
                    values.append(d)
            else:
                values.append(0)
            return tuple(values)

        ans = defaultdict(list)
        for string in strings:
            ans[count_hash(string)].append(string)
        return list(ans.values())

print(Solution().groupStrings(["aa", "bb", "b"]))