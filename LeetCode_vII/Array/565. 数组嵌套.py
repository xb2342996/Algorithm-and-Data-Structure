# written by xiongbiao
# date 2020-10-23

class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curLength = 0
        maxLength = 0

        visited = [0] * len(nums)
        current_index = 0

        while 0 in visited:
            if visited[current_index] == 0:
                curLength += 1
                visited[current_index] = 1
                current_index = nums[current_index]
            else:
                maxLength = max(curLength, maxLength)
                current_index = self.findNextZero(visited)
                curLength = 0
        maxLength = max(curLength, maxLength)
        return maxLength


    def findNextZero(self, visited):
        for i, v in enumerate(visited):
            if v == 0:
                return i


print(Solution().arrayNesting([0, 2, 1]))