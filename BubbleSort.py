def bubble_sort(data_list):
    for r in range(1,len(data_list)):        #defining the rounds which is data_list-1
        for i in range(len(data_list)-r):    #defining the no of comparisons starting from n-1
            if data_list[i]>data_list[i+1]:
                data_list[i],data_list[i+1]=data_list[i+1],data_list[i]
                
def modified_bubble_sort(data_list):
    flag=False
    for r in range(1,len(data_list)):        #defining the rounds which is data_list-1
        flag=False
        for i in range(len(data_list)-r):    #defining the no of comparisons starting from n-1
            if data_list[i]>data_list[i+1]:
                data_list[i],data_list[i+1]=data_list[i+1],data_list[i]
                flag=True
        if not flag:
            break
        
                
l= [43,25,53,88,20,11]
bubble_sort(l)
print(l)
modified_bubble_sort(l)
print(l)