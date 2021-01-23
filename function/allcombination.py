import itertools

def combination(l, r):
    count = 1
    for i in range(len(mylist)+1):
        if i==r:
            for i in itertools.combinations(mylist, i):
                print("%2d: %s" %(count, i))
                count += 1


if __name__ == '__main__':
    mylist = [1,2,3,4]
    count = 1
    for i in range(len(mylist)+1):
        for i in itertools.combinations(mylist, i):
            print("%2d: %s" %(count, i))
            count += 1

    combination(mylist, 3)