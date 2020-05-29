## written by xiongbiao
## date 2020-5-29

'''
给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
'''

class Solution(object):
    '''
    思路：清除小于等于0和大于n的数字，数组索引的值作为索引指向的元素的正负代表了这个元素是否存在
    检查 1 是否存在于数组中。如果没有，则已经完成，1 即为答案。
    如果 nums = [1]，答案即为 2 。
    将负数，零，和大于 n 的数替换为 1 。
    遍历数组。当读到数字 a 时，替换第 a 个元素的符号。
    注意重复元素：只能改变一次符号。由于没有下标 n ，使用下标 0 的元素保存是否存在数字 n。
    再次遍历数组。返回第一个正数元素的下标。
    如果 nums[0] > 0，则返回 n 。
    如果之前的步骤中没有发现 nums 中有正数元素，则返回n + 1。
    '''
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        if 1 not in nums:
            return 1

        if len(nums) == 1:
            return 2

        for i in range(length):
            if nums[i] <= 0 or nums[i] > length:
                nums[i] = 1

        for i in range(length):
            index = abs(nums[i])

            if index == length:
                nums[0] = -abs(nums[0])
            else:
                nums[index] = -abs(nums[index])

        for i in range(1, length):
            if nums[i] > 0:
                return i

        if nums[0] > 0:
            return length

        return length + 1

