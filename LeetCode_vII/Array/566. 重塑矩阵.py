# written by xiongbiao
# date 2020-10-26

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        row = len(nums)
        col = len(nums[0])
        if col * row != r * c:
            return nums

        dim_1 = []
        for i in range(row):
            dim_1.extend(nums[i])
        reshape = [[0] * c for _ in range(r)]
        last = int(len(dim_1) / r) - 1
        print(last)
        line = 0
        count = 0
        for i, e in enumerate(dim_1):
            reshape[line][count] = e
            if count == last:
                line += 1
                count = 0
            else:
                count += 1

        return reshape

print(Solution().matrixReshape([[1,2], [3, 4]], 1, 4))