def duplicate( a ):
    for i in a :
        if (a.count(i) > 1):
            print("element {} is repeated".format(i))

duplicate([1,2,3,4,5,3])