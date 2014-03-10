def isPrime (num):
    snum = str (num)
    if snum [-1] == 0 or snum [-1] == 2 or snum [-1] == 4 or snum [-1] == 5 or snum [-1] == 6 or snum [-1] == 8:
        return False
    if sum ([int (a) for a in snum]) % 3 == 0:
        return False
    if int (snum[:-1]) - (int (snum[-1]) * 2) % 7 == 0:
        return False
    return True

def listOfCombinations (toCombine):
    if len (toCombine) == 1:
        return [[toCombine [0]]]
    r = []
    for a in range (len (toCombine)):
        p1 = listOfCombinations (toCombine[:a] + toCombine [a+1:])
        p2 = [toCombine [a]]
        for a in p1:
            r += [p2 + a]
    return r

def listOfStringCombinations (string):
    combos = listOfCombinations ([a for a in string])
    r = []
    for a in combos:
        toAdd = ""
        for b in a:
            toAdd += b [0]
        r += [toAdd]
    return r

def merge (a, b):
    aID = 0
    bID = 0
    c = []
    while (True):
        if a [aID] < b [bID]:
            c += [a [aID]]
            aID += 1
            if aID == len (a):
                for i in range (bID, len (b)):
                    c += [b [i]]
                return c
        else:
            c += [b [bID]]
            bID += 1
            if bID == len (b):
                for i in range (aID, len (a)):
                    c += [a [aID]]
                return c

def mergeSort (toSort):
    if len (toSort) == 1:
        return toSort
    a = mergeSort (toSort [:len (toSort) / 2])
    b = mergeSort (toSort [len (toSort) / 2:])
    return merge (a, b)

found = False
for a in range (9, 0, -1):
    print "constructing list of ", a, "pandigital numbers"
    pandigitals = [int (b) for b in listOfStringCombinations ('123456789'[:a])]
    pandigitals = mergeSort (pandigitals)
    print "checking if any are prime"
    for b in range (len (pandigitals) - 1, 0, -1):
        if isPrime (pandigitals [b]):
            print pandigitals [b], 'is prime'
            found = True
            break
    if found:
        break
