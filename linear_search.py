def linear_search(nList,nNum):
    for index,element in enumerate(nList):
        if nNum==element:
            return index
    return False
nList=[12,4,5,232,1,51,67645,3,111,35]
nNum=51
print(linear_search(nList,nNum))