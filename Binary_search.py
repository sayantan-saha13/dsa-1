def binary_search(nList,nSearch):
    left_index=0
    right_index=len(nList)-1
    mid_index=0
    while left_index<=right_index:
       mid_index=(left_index+right_index)//2
       mid_number=nList[mid_index]
       if mid_number==nSearch:
           return mid_index
       if mid_number<nSearch:
           left_index=mid_index+1
       else:
           right_index=mid_index-1
    return -1
arr=[21,34,65,686,4534,24566]
search=4534
print(binary_search(arr,search))