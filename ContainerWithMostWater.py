__author__ = 'wxy325'
class Solution:
    # @return an integer
    def maxArea(self, height):          #n ln n
        sortedHeight = sorted(height)   #ln n
        hDict = {}
        lDict = {}

        #n ln n
        for i in range(len(height) - 1, -1, -1):
            num = height[i]
            if not num in hDict:
                hDict[num] = i

        #n ln n
        for i in range(len(height) - 2, -1, -1):
            h = sortedHeight[i]
            hb = sortedHeight[i + 1]
            l = hDict[h]
            lb = hDict[hb]
            if lb > l:
                hDict[h] = lb



        #n ln n
        for i in range(0,len(height)):
            num = height[i]
            if not num in lDict:
                lDict[num] = i

        #n ln n
        for i in range(len(height) - 2, -1, -1):
            h = sortedHeight[i]
            hb = sortedHeight[i + 1]
            l = lDict[h]
            lb = lDict[hb]
            if lb < l:
                lDict[h] = lb

        maxArea = 0
        for i in range(0, len(height)):
            h = height[i]
            l2 = hDict[h]
            l1 = lDict[h]
            area = h * (l2 - l1)
            if area > maxArea:
                maxArea = area

        return maxArea

if __name__ == '__main__':
    s = Solution()
    #assert s.maxArea([2,3,4]) == 4
    #assert s.maxArea([2,3,4,2,5]) == 9
    assert s.maxArea([10,9,8,7,6,5,4,3,2,1]) == 25