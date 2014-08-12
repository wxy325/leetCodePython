__author__ = 'wxy325'
class Solution:
    # @return an integer
    def atoi(self, str):

        fStr = str.strip()
        # fStr = ''.join(str.split(' '))
        if len(fStr) == 0:
            return 0
        f = 1
        # while len(fStr) != 0:
        if fStr[0] == '-':
            f *= -1
            fStr = fStr[1:]
        elif fStr[0] == '+':
            f *= 1
            fStr = fStr[1:]
            # else:
            #     break;
        fResult = 0
        try:
            for n in range(0, len(fStr)):
                fResult *= 10
                fResult += int(fStr[n])
        except ValueError:
            fResult /= 10
            pass
        fResult = fResult * f
        if fResult > 2147483647:
            fResult = 2147483647
        if fResult < -2147483648:
            fResult = -2147483648
        return fResult

if __name__ == '__main__':
    s = Solution()
    assert s.atoi('  123a22  ') == 123
    assert s.atoi("") == 0
    assert s.atoi(" + 0123") == 0
    assert s.atoi(" + -123") == 0
    assert s.atoi("   ") == 0
    assert s.atoi('  123  ') == 123

    assert s.atoi(' - 431 ') == 0