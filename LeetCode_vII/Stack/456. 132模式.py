## written by xiongbiao
## date 2020-5-30
'''
给定一个整数序列：a1, a2, ..., an，一个132模式的子序列 ai, aj, ak 被定义为：当 i < j < k 时，ai < ak < aj。设计一个算法，
当给定有 n 个数字的序列时，验证这个序列中是否含有132模式的子序列。
'''
class Solution(object):
    '''
    记录每个位置的左边最小值，从后向前遍历列表中的每个数字，构成一个单调递减栈找到最大的次大值，如果构成当 i < j < k 时，ai < ak < aj返回True
    '''
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        size = len(nums)
        leftMins = [0] * size
        leftMins[0] = nums[0]
        for i in range(1, size):
            leftMins[i] = min(nums[i], leftMins[i-1])
        print(leftMins)
        stack = []
        for i in range(size)[::-1]:
            while len(stack) > 0 and nums[i] > nums[stack[-1]]:
                if leftMins[i] < nums[i] and leftMins[i] < nums[stack[-1]]:
                    return True
                stack.pop()
            stack.append(i)
        return False

print(Solution().find132pattern([-2, 1, -1]))