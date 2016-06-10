class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        #midIndex = (len(A) + len(B) + 1) / 2
        pass



if __name__ == '__main__':
    s = Solution()
    assert s.findMedianSortedArrays([1, 2, 3], [3, 4, 5]) == 3
    assert s.findMedianSortedArrays([0, 12, 100],[1, 9, 15, 16]) == 12