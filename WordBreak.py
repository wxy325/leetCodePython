class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, word_dict):
        return self.word_break_helper(s, word_dict, {})

    def word_break_helper(self, s, word_dict, record_dict):
        if s in record_dict:
            return record_dict[s]

        fRet = False
        for word in word_dict:
            firstWord = s[:len(word)]
            if firstWord == word:
                subStr = s[len(word):]
                if len(subStr):
                    f = self.word_break_helper(subStr, word_dict, record_dict)
                    if f:
                        record_dict[s] = True
                        return True
                else:
                    record_dict[s] = True
                    return True
            else:
                continue
        record_dict[s] = fRet
        return fRet


if __name__ == '__main__':
    s = Solution()
    assert not s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])