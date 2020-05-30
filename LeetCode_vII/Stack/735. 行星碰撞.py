## written by xiongbiao
## date 2020-5-30
'''
给定一个整数数组 asteroids，表示在同一行的行星。
对于数组中的每一个元素，其绝对值表示行星的大小，正负表示行星的移动方向（正表示向右移动，负表示向左移动）。每一颗行星以相同的速度移动。
找出碰撞后剩下的所有行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。
'''
class Solution(object):
    '''
    单调栈，行星撞击有3种情况，大于小于等于
    '''
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for n in asteroids:
            while stack and stack[-1] > 0 and n < 0:
                if abs(stack[-1]) < abs(n):
                    stack.pop()
                elif abs(stack[-1]) == abs(n):
                    stack.pop()
                break
            else:
                stack.append(n)

        return stack

Solution().asteroidCollision([8, -8])