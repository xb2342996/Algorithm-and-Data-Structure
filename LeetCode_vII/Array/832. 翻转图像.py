"""
@author: xiongbiao
@date: 2021-04-22 21:26
"""

class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        size = len(image)
        for im in image:
            left, right = 0, size - 1
            while left < size / 2:
                im[left], im[right] = im[right] ^ 1, im[left] ^ 1
                left += 1
                right -= 1
        return image

print(Solution().flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))

