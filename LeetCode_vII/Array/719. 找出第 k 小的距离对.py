## written by xiongbiao
## date 2020-5-28

'''
给定一个整数数组，返回所有数对之间的第 k 个最小距离。一对 (A, B) 的距离被定义为 A 和 B 之间的绝对差值。
'''
class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """ # [1,4,5,6,10,12,19,20,22]
        if nums is None or len(nums) == 0 or k > len(nums) * (len(nums) - 1) / 2:
            return None

        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left < right:

            mid = (left + right) >> 1

            count, start = 0, 0
            for i in range(len(nums)):
                while nums[i] - nums[start] > mid:
                    start += 1
                count += i - start

            if count < k:
                left = mid + 1
            else:
                right = mid
        return left

    '''
    排序计算2个数之间的差，使用堆排序进行排列
    时间复杂度O(NlogN）空间复杂度O（N^2)
    '''
    # def smallestDistancePair(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: int
    #     """
    #     import heapq
    #
    #     if nums is None or len(nums) == 0 or k > len(nums) * (len(nums) - 1) / 2:
    #         return None
    #
    #     nums.sort()
    #     dis = []
    #     for i in range(1, len(nums)):
    #         dis.append((nums[i] - nums[i - 1], i-1, i))
    #
    #     heapq.heapify(dis)
    #     for _ in range(k):
    #         d, i, j = heapq.heappop(dis)
    #         if j + 1 < len(nums):
    #             heapq.heappush(dis, (nums[j+1] - nums[i], i, j + 1))
    #
    #     return d




print(Solution().smallestDistancePair([1,4,5,6,10,12,19,20,22], 3))
