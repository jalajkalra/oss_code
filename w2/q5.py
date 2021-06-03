def lensort(slist) :
    for j in range(0,len(slist)):
        pos = j
        minlen = len(slist[j])
        for i in range(j,len(slist)):
            if(minlen > len(slist[i])):
                pos = i
                minlen = len(slist[i])
        temp = slist[j]
        slist[j] = slist[pos]
        slist[pos] = temp
    return slist
print(lensort(["hello","world","from","Eshan Dhawan"]))