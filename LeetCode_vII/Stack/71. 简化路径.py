## written by xiongbiao
## date 2020-5-30
'''
以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径。
在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）
两者都可以是复杂相对路径的组成部分。更多信息请参阅：Linux / Unix中的绝对路径 vs 相对路径
'''
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        path += '/'
        path = list(path)
        dir = ''
        for s in path:
            if s == '/':
                if dir == '.':
                    dir = ''
                    continue
                elif dir == '..':
                    if stack:
                        stack.pop()
                elif dir != '':
                    stack.append(dir)
                dir = ''
                if stack and stack[-1] != '/':
                    continue
            else:
                dir += s


        return '/' + '/'.join(stack)

print(Solution().simplifyPath("/home/foo/.ssh/authorized_keys/"))

