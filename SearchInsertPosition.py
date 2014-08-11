__author__ = 'wxy325'
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if len(A) == 0:
            return 0
        if target < A[0]:
            return 0
        return self.searchF(A, target, 0, len(A))

    def searchF(self, A, target, fromIndex, toIndex):
        if A[fromIndex] == target:
            return fromIndex
        if fromIndex == toIndex - 1:
            return fromIndex + 1


        mid = (fromIndex + toIndex) / 2
        v = A[mid]
        if v > target:
            return self.searchF(A, target, fromIndex, mid)
        else:
            return self.searchF(A, target, mid, toIndex)

if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1,3], 2))