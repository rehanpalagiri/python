def ps(N):
    index=1
    while (index <= N):
        print ("hello: ", index)
        index = index +1 
ps(5)  

def sumOfNumbers(n):
    index=1
    sum=0
    while (index<=n):
        sum = sum + index 
        index = index + 1
    return sum 

s = sumOfNumbers(5)
print ("first 5 natural numbers",s)

s = sumOfNumbers(3)
print ("first 3 natural numbers",s)


def printEvenNumbers(n):
    index=1
    while (index <= n):
        if index%2==0:
            print (index)
        index= index +1 
print("even numbers till 5 are: ")
printEvenNumbers(5)
print("even numbers till 10 are: ")
printEvenNumbers(10)
