# Wrute a recursive function to print first Natural numbers

def printN(n):
    if n>0:
        printN(n-1)
        print(n,end=' ')
printN(10) 
print()
#o/p: 1 2 3 4 5 6 7 8 9 10 

# Write a recursive function to print first N natural number in reverse order
def printNreverse(n):
    if n>0:
        print(n,end=' ')
        printNreverse(n-1)
printNreverse(10)
print()
#o/p: 10 9 8 7 6 5 4 3 2 1

# Write a recursive function to print first odd natural numbers
def printNOdd(n):
    if n>0:
        printNOdd(n-1)
        print(2*n-1,end=' ')
printNOdd(10)
print()
#o/p: 1 3 5 7 9 11 13 15 17 19

# Write a recursive function to print first even natural numbers 
def printNeven(n):
    if n>0:
        printNeven(n-1)
        print(2*n,end=' ')
printNeven(10)
print()
#o/p: 2 4 6 8 10 12 14 16 18 20

# Write a recursive function to print first odd natural numbers in reverse
def printNOdd(n):
    if n>0:
        print(2*n-1,end=' ')
        printNOdd(n-1)        
printNOdd(10)
print()
#o/p: 19 17 15 13 11 9 7 5 3 1

# Write a recursive function to print first even natural numbers in reverse
def printNeven(n):
    if n>0:
        print(2*n,end=' ')
        printNeven(n-1)        
printNeven(10)
print()
#o/p: 20 18 16 14 12 10 8 6 4 2

# write a recursive function to calculate sum of N natural Numbers
def sumN(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return n+sumN(n-1)
print("sum is",sumN(10))
# o/p: sum is 55

# write a recursive function to calculate sum of N odd natural Numbers
def sumNOdd(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return 2*n-1 +sumNOdd(n-1)
print("sum is",sumNOdd(10))
# o/p: sum is 100

# write a recursive function to calculate sum of N even natural Numbers
def sumNEven(n):
    if n==0:
        return 0
    if n==1:
        return 2
    return 2*n +sumNEven(n-1)
print("sum is",sumNEven(10))
# o/p: sum is 110

# write a recursive function to calculate factorial of a Numbers
def Fact(n):
    if n==0:
        return 1
    return n * Fact(n-1)
print("Factorial is", Fact(5))
# o/p: Factorial is 120

# write a recursive function to calculate sum of square of N natural Numbers
def sumNSquare(n):
    if n==1:
        return 1
    return n*n + sumNSquare(n-1)
print("sum of square is", sumNSquare(5))
# o/p: sum of square is 55