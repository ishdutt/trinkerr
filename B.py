def isAnagram(s1, s2) :
    if len(s1) != len(s2):
        return False
    charOccuranceCount1 = {}
    for chr in s1:
        if chr not in charOccuranceCount1.keys():
            charOccuranceCount1[chr] = 0
        else:    
            charOccuranceCount1[chr] = charOccuranceCount1[chr] + 1

    charOccuranceCount2 = {}
    for chr in s2:
        if chr not in charOccuranceCount2.keys():
            charOccuranceCount2[chr] = 0
        else:    
            charOccuranceCount2[chr] = charOccuranceCount2[chr] + 1

    for i in charOccuranceCount1 :
        if i not in charOccuranceCount2.keys():
            return False
        if charOccuranceCount1[i] is not charOccuranceCount2[i]:
            return False
    
    return True


inString = input();
arrayString = inString.split(", ");
listOfKeys = list()

for string in  arrayString :
    openBrackFound = False
    res = ""
    for chr in string :
        if chr == '"' :
            openBrackFound = not openBrackFound
            continue
        if openBrackFound :
            res += chr
    listOfKeys.append(res)

n = len(listOfKeys)
anagramList = list()
singleList = list()

for i in range(n):
    if listOfKeys[i] == " ":
        continue
    if i == n-1:
        singleList.append(listOfKeys[i])
    for j in range(i + 1, n):
        key1 = listOfKeys[i]
        key2 = listOfKeys[j]
        if isAnagram(key1, key2):
            lis = list()
            lis.append(key1)
            lis.append(key2)
            anagramList.append(lis)
            listOfKeys[j] = " "
            break
        else:
            singleList.append(listOfKeys[i])

anagramList = anagramList + singleList

print(anagramList)