"""
Given two strings. Using operations delete, insert, replace change second string to be equal to the first string
table
tble


"""


# top-down approach
def num_of_operations(s1: str, s2: str, ind1: int, ind2: int, meta: dict = None) -> int:
    if meta is None:
        meta = {}
    if ind1 == len(s1):
        return len(s2) - ind2
    if ind2 == len(s2):
        return len(s1) - ind1
    if s1[ind1] == s2[ind2]:
        return num_of_operations(s1, s2, ind1 + 1, ind2 + 1, meta)

    meta_key = str(ind1) + str(ind2)
    if meta_key not in meta.keys():
        del_char = num_of_operations(s1, s2, ind1, ind2 + 1, meta)
        add_char = num_of_operations(s1, s2, ind1 + 1, ind2, meta)
        rep_char = num_of_operations(s1, s2, ind1 + 1, ind2 + 1, meta)
        meta[meta_key] = 1 + min(del_char, add_char, rep_char)

    return meta[meta_key]


# bottom-up approach
def findMinOperationBU(s1, s2, tempDict):
    for i1 in range(len(s1) + 1):
        dictKey = str(i1) + '0'
        tempDict[dictKey] = i1
    for i2 in range(len(s2) + 1):
        dictKey = '0' + str(i2)
        tempDict[dictKey] = i2

    for i1 in range(1, len(s1) + 1):
        for i2 in range(1, len(s2) + 1):
            if s1[i1 - 1] == s2[i2 - 1]:
                dictKey = str(i1) + str(i2)
                dictKey1 = str(i1 - 1) + str(i2 - 1)
                tempDict[dictKey] = tempDict[dictKey1]
            else:
                dictKey = str(i1) + str(i2)
                dictKeyD = str(i1 - 1) + str(i2)
                dictKeyI = str(i1) + str(i2 - 1)
                dictKeyR = str(i1 - 1) + str(i2 - 1)
                tempDict[dictKey] = 1 + min(tempDict[dictKeyD], min(tempDict[dictKeyI], tempDict[dictKeyR]))
    dictKey = str(len(s1)) + str(len(s2))
    return tempDict[dictKey]


# unfinished
def convert(s1: str, s2: str):
    meta = {}
    i = 0
    j = 0

    meta_key = str(i) + str(j)
    if s1[i] == s2[j]:
        meta[meta_key] = 0
    else:

        if meta_key not in meta.keys():
            add_key = str(i) + str(j - 1)
            del_key = str(i - 1) + str(j)
            rep_key = str(i - 1) + str(j - 1)
            meta[meta_key] = 1 + min(meta[del_key], meta[add_key], meta[rep_key])


str1 = "table"
str2 = "tblred"
print(num_of_operations(str1, str2, 0, 0))
meta = {}
findMinOperationBU(str1, str2, meta)
print(meta)
