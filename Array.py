# Given an array with some integer type values. Write a python script values?

import array as ar
a=ar.array('i',[76,345,6,77,13])
b=list(a)
b.sort()
c=ar.array('i',b)
print(c)

# Output:
# array('i', [6, 13, 76, 77, 345])


# Given a list of heterogenous elements. Write a python script to remove all the non int values from the list.

z=7
x=['mohit',1,2,3,'harshal',35]
new_x=[]
for i in x:
    if type(i)==type(z):
        new_x.append(i)
print(new_x)  

# Output:
# [1, 2, 3, 35]


# Write a Python script to calculate avg of elements of a list      

m=[23,34,45,56,67]
avg= sum(m)/len(m)
print("average of list is :",avg)

# Output
# average of list is : 45.0


# Write a Python script to create a list of first N prime number

n=int(input('enter the value :'))
lx = []
for i in range(2,n+1):
    count=0
    for j in range(2,i):
        if (i%j)==0:
            count=+1
    if count==0:
        lx.append(i)
print(lx)   

# also  

import math
lm=[]
def check_prime(n):
    if n==1:
        return 'not prime'
    for i in range(2,round(math.sqrt(n))+1):
        if n%i ==0:
            return 'not prime'
            break
    else:
       return not 'check_prime'
   
cp=check_prime(float (input('enter the value :'))) 
print(cp) 

# Output
# enter the value :10
# not prime
  
              
# Write a Python script to create a list of first N terms of a fibonacci series

fibo=10
a=0
b=1
result=[a,b]
for i in range(2,fibo):
    result.append(result[-1]+result[-2])
print (result)  

# Output
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] 
