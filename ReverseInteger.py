__author__ = 'wxy325'
class Solution:
    # @return an integer
    def reverse(self, x):
        st = str(x)
        if st[0] == '-':
            n = st[1:]
            f = '-'
        else:
            n = st
            f = ''
        return int(f + n[-1::-1] )


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-123))