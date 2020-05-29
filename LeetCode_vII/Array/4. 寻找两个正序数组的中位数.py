## written by xiongbiao
## date 2020-5-29

class Solution(object):

    '''
    左右边界位0和第一个数组的长度，二分法寻找到第一个数组的中位数分割，根据2个数组的和计算第二个中位数分割的位置如果
    第一个数组分割的左边大于第二个数组分割的右边，第一个数组的右边界变为第一个数组分割的位置，否则左边界变为第一个数组分割位置的右侧
    找到位置后比较分割位置的左侧的最大值和分割右侧的最小值，根据长度计算中位数
    '''
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        total = (m + n + 1) >> 1

        left = 0
        right = m
        while left < right:
            i = ((left + right + 1) >> 1)
            j = total - i
            if nums1[i - 1] > nums2[j]:
                right = i - 1
            else:
                left = i

        i = left
        j = total - i
        nums1LeftMax = nums1[i - 1] if i != 0 else float('-inf')
        nums1RightMin = nums1[i] if i != m else float('inf')
        nums2LeftMax = nums2[j - 1] if j != 0 else float('-inf')
        nums2RightMin = nums2[j] if j != n else float('inf')

        if (m + n) % 2 == 0:
            return float((max(nums1LeftMax, nums2LeftMax) + min(nums1RightMin, nums2RightMin)) / 2)
        else:
            return max(nums2LeftMax, nums1LeftMax)

print(Solution().findMedianSortedArrays([1,2], [3,4]))