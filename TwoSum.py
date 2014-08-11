__author__ = 'wxy325'
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        if len(num) < 2:
            return None
        aDict = {}
        for i in range(0, len(num)):
            aDict[num[i]] = i

        for i in range(0, len(num)):
            t = target - num[i]
            if t in aDict:
                ind = aDict[t]
                if i < ind:
                    return (i+1, ind+1)
                elif i > ind:
                    return (ind+1, i+1)
        return None

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3,2,4], 6))