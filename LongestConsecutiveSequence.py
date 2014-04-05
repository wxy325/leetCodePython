

if __name__ == '__main__':
    num = [9,1,-3,2,4,8,3,-1,6,-2,-4,7]

    num = list(set(num))
    num.sort()

    fFirst = True

    for n in num:
        if fFirst:
            count = 1
            maxCount = 1
            fFirst = False
            pass
        else:
            if pre + 1 == n:
                count = count + 1
            else:
                if maxCount < count:
                    maxCount = count
                count = 1
        pre = n

    if maxCount < count:
        maxCount = count
        count = 1
    print(maxCount)