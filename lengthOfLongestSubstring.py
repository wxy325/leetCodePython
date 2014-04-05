def lengthOfLongestSubstring(s):
    if len(s)==0:
        return 0


    subStr = s[0]
    count = 1
    maxCount = 1
    for c in s[1:]:
        if c not in subStr:
            subStr = subStr + c
            count = count +1
        else:
            if maxCount < count:
                maxCount = count

            newIndex = subStr.find(c)
            count = count - newIndex
            subStr = subStr[newIndex+1:] + c

    if maxCount < count:
        maxCount = count
    return maxCount


if __name__ == '__main__':
    s = 'abcabcbb'
    print(lengthOfLongestSubstring(s))