def store(str):
    strDict = {}
    for i in str:
        if(strDict.get(i, 0)):
            count = strDict.get(i)
            strDict.update({i: count+1})
        else:
            strDict.update({i: 1})
    return strDict

# FIRST NON REPEATED
def firstNonRepeated(str):
    strDict = store(str)
    
    for i in str:
        if(strDict.get(i) == 1):
            print(i)
            return
    print("None")

# firstNonRepeated("hehheheh")
# firstNonRepeated("My name is hehheheh")


# FIRST REPEATED
def firstRepeated(str):
    strDict = store(str)

    for i in str:
        if(strDict.get(i) > 1):
            print(i)
            return
    print("None")

# firstRepeated("hehehehe")
# firstRepeated("My name is hehehehe")


# MOST REPEATED
def mostRepeated(str):
    strDict = store(str)

    for i in str:
        max = 0
        maxChar = ''
        get = strDict.get(i)
        if(get > max):
            max = get
            maxChar = i
    print(maxChar)

# mostRepeated("My name is hehehehhhhhhh")


# COUNT UNIQUE PAIRS WITH DIFFRENCE K
def countPairsWithDiffK(list, k):
    count = 0
    numberSet = set()
    numberSetCopy = set()
    for i in list:
        numberSet.add(i)
        numberSetCopy.add(i)
    
    for i in numberSetCopy:
        if(i + k in numberSet):
            count+=1
        if(i - k in numberSet):
            count+=1
        numberSet.remove(i)
    print(count)

# list = [1, 7, 5, 9, 2, 12, 3]
# countPairsWithDiffK(list,2)


# INDICES OF PAIRS THAT ADD UP TO K
def twoSumK(list, k):
    numberSet = set()
    for i in list:
        numberSet.add(i)
    
    for i in range(len(list)):
        res = k - list[i]
        if(res in numberSet):
            print(i, list.index(res))
        numberSet.remove(list[i])

list = [2, 7, 11, 15]
twoSumK(list,9)