__author__ = 'wxy325'
class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        if path == '':
            return '/'
        pathArray = path.split('/')
        outArray = []
        outputPath = ''
        for p in pathArray:
            if p == '' or p == '.':
                continue
            elif p == '..':
                if len(outArray) > 0:
                    outArray.pop()
            else:
                outArray.append(p)

        for p in outArray:
            outputPath += '/' + p
        if outputPath == '':
            outputPath = '/'
        return outputPath


if __name__ == '__main__':
    s = Solution()
    assert s.simplifyPath('//') == '/'
    assert s.simplifyPath('/../') == '/'
    assert s.simplifyPath('/a/..') == '/'
    assert s.simplifyPath('/a/.') == '/a'
    assert s.simplifyPath('/a/../c') == '/c'