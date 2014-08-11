__author__ = 'wxy325'
class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if len(triangle) == 1:
            return triangle[0][0]
        if len(triangle) == 2:
            return triangle[0][0] + min(triangle[1])

        for row in range(len(triangle) -2, -1, -1):
            for column in range(0, len(triangle[row])):
                if triangle[row + 1][column] < triangle[row + 1][column + 1]:
                    triangle[row][column] += triangle[row + 1][column]
                else:
                    triangle[row][column] += triangle[row + 1][column + 1]

        return triangle[0][0]

if __name__ == '__main__':
    s = Solution()
    a = s.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
])
    print(a)