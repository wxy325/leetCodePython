__author__ = 'wxy325'
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        resultArray = [0, 1, 2]

        if n < 3:
            return resultArray[n]
        else:
            i = 3

            a1 = 1
            a2 = 2
            a3 = 3
            while True:

                if i == n:
                    return a3
                else:
                    a1 = a2
                    a2 = a3
                    a3 = a1 + a2
                    i += 1

if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(4))
