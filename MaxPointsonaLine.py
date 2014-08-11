__author__ = 'wxy325'
# Definition for a point


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
'''
class Record:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    def compK(self, r):
        deltX = self.point2.x - self.point1.x
        deltY = self.point2.y - self.point1.y

        rDeltaX = r.point2.x - r.point1.x
        rDeltaY = r.point2.y - r.point1.y

        return rDeltaX * deltY == rDeltaY * deltX

    def compP(self, r):
        for point in [self.point1, self.point2]:
            for pointR in [r.point1, r.point2]:
                if point.x == pointR.x and point.y == pointR.y:
                    return True
        return False



class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        recordArray = [];
        for i in range(0, len(points)):
            for j in range(i + 1, len(points)):
                r = Record(points[i], points[j])

                fHave = False

                for arr in recordArray:
                    if (arr[0].compK(r)):
                        arr.append(r)
                        fHave = True
                if not fHave:
                    recordArray.append([r])


        maxCount = 0
        for arr in recordArray:
            tempArr = []
            for a in arr:
                f = False

                for tempSet in tempArr:

                    if a.point1 in tempSet:
                        tempSet.add(a.point2)
                        f = True
                        break

                    if a.point1 in tempSet:
                        tempSet.add(a.point1)
                        f = True
                        break
                if not f:
                    tempArr.append({a.point1, a.point2})

            m = max(len(b) for b in tempArr)
            if m > maxCount:
                maxCount = m


        return maxCount



        #c = [[i1, i2] for i1 in a i2 in b]]

        #r1 = Record(Point(1,2),Point(3,4))
        #r2 = Record(Point(3,4),Point(5,6))
        #if (r1.compP(r2)):
        #   print("bbb")
'''

class Solution:
    # @param points, a list of Points
    # @return an integer
        def maxPoints(self, points):
            if len(points) <= 2:
                return len(points)
            max_count = 0
            for i in range(0,len(points)):

                dup = 1
                kMap = {}
                infin = 0

                pointI = points[i]
                for j in range(i+1, len(points)):
                    pointJ = points[j]

                    if pointI.x == pointJ.x and pointI.y == pointJ.y:
                        dup += 1
                        continue
                    if pointI.x == pointJ.x:
                        infin += 1
                    else:
                        k = (float)(pointJ.y - pointI.y) / (pointJ.x - pointI.x)
                        if k in kMap:
                            kMap[k] += 1
                        else:
                            kMap[k] = 1
                t = [kMap[a1] for a1 in kMap]
                if len(t):
                    maxF = max(t)
                else:
                    maxF = 0
                if infin > maxF:
                    maxF = infin
                if maxF + dup > max_count:
                    max_count = maxF + dup
            return max_count





if __name__ == '__main__':
    s = Solution()

    print(s.maxPoints([Point(0, 0), Point(1, 1), Point(1, -1)]))
