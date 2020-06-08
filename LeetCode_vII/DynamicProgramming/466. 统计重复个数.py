## written by xiongbiao
## date 2020-6-8

'''
由 n 个连接的字符串 s 组成字符串 S，记作 S = [s,n]。例如，["abc",3]=“abcabcabc”。
如果我们可以从 s2 中删除某些字符使其变为 s1，则称字符串 s1 可以从字符串 s2 获得。例如，根据定义，"abc" 可以从 “abdbec” 获得，但不能从 “acbbe” 获得。
现在给你两个非空字符串 s1 和 s2（每个最多 100 个字符长）和两个整数 0 ≤ n1 ≤ 106 和 1 ≤ n2 ≤ 106。现在考虑字符串 S1 和 S2，其中 S1=[s1,n1] 、S2=[s2,n2] 。
请你找出一个可以满足使[S2,M] 从 S1 获得的最大整数 M 。
'''
class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        if n1 == 0:
            return 0
        s2_index = 0
        s1_count, s2_count = 0, 0
        loop_point = {}
        while True:
            s1_count += 1
            for i in range(len(s1)):
                if s1[i] == s2[s2_index]:
                    s2_index += 1
                    if s2_index == len(s2):
                        s2_count += 1
                        s2_index = 0

            if s1_count == n1:
                return s2_count // n2

            if s2_index in loop_point:
                s1_prev, s2_prev = loop_point[s2_index]
                prev_loop = (s1_prev, s2_prev)
                in_loop = (s1_count - s1_prev, s2_count - s2_prev)

                break
            else:
                loop_point[s2_index] = (s1_count, s2_count)

        ans = prev_loop[1] + (n1 - prev_loop[0]) / in_loop[0] * in_loop[1]
        rest = (n1 - prev_loop[0]) % in_loop[0]
        for i in range(rest):
            for s in s1:
                if s == s2[s2_index]:
                    s2_index += 1
                    if s2_index == len(s2):
                        ans += 1
                        s2_index = 0
        return ans // n2


print(Solution().getMaxRepetitions('acb', 4, 'ab', 2))