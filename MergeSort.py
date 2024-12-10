def merge_sort(list1):
    if len(list1)>1:
        mid=len(list1)//2
        leftlist=list1[:mid]
        rightlist=list1[mid:]
        
        merge_sort(leftlist)
        merge_sort(rightlist)
        
        i=j=k=0            #here i,j,k are working as index
        while i<len(leftlist) and j<len(rightlist):
            if leftlist[i]<rightlist[j]:
                list1[k]=leftlist[i]
                i+=1
            else:
                list1[k]=rightlist[j]
                j+=1
            k+=1
        while i<len(leftlist):
            list1[k]=leftlist[i]
            i+=1
            k+=1
        while j<len(rightlist):
            list1[k]=rightlist[j]
            j+=1
            k+=1
            
mylist=[75,29,83,42,16,90,56,34,20,71,88,92,7]
merge_sort(mylist)
print(mylist)

# O/p:    [7, 16, 20, 29, 34, 42, 56, 71, 75, 83, 88, 90, 92]

            
            