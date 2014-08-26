__author__ = 'wxy325'
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dictionary):
        recordArray = []
        strLength = len(s)
        for sIndex in range(0, len(s)):
            indexArray = []
            for word in dictionary:
                wordLength = len(word)
                if sIndex + wordLength > strLength:
                    pass
                else:
                    if s[sIndex:sIndex + wordLength] == word:
                        indexArray.append(word)
            recordArray.append(indexArray)

        retArray = self.break_word(recordArray, 0, {})
        return retArray


    def break_word(self, recordArray, currentIndex, recordDict):
        if currentIndex in recordDict:
            return recordDict[currentIndex]
        else:
            retArray = []
            for word in recordArray[currentIndex]:
                newLength = currentIndex + len(word)
                if newLength > len(recordArray):
                    continue
                elif newLength == len(recordArray):
                    retArray.append(word)
                elif recordArray[newLength] != None:
                    tArray = self.break_word(recordArray, newLength, recordDict)
                    retArray = retArray + [word + ' ' + w for w in tArray]
            recordDict[currentIndex] = retArray
            return retArray

if __name__ == '__main__':
    s = Solution()

    print(s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))