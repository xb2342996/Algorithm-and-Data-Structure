## written by xiongbiao
## date 2020-5-31

'''
返回 A 的最短的非空连续子数组的长度，该子数组的和至少为 K 。
如果没有和至少为 K 的非空子数组，返回 -1 。
'''
class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if len(A) == 0:
            return -1

        prefixSum = [0] * (len(A) + 1)
        for i in range(len(A)):
            prefixSum[i + 1] = prefixSum[i] + A[i]

        deque = []
        ans = len(prefixSum)
        for i, p in enumerate(prefixSum):
            while deque and p - prefixSum[deque[0]] >= K:
                ans = min(ans, i - deque.pop(0))
            while deque and p <= prefixSum[deque[-1]]:
                deque.pop()
            deque.append(i)
        return -1 if ans == len(A) + 1 else ans


Solution().shortestSubarray([2,-1,2], 3)
