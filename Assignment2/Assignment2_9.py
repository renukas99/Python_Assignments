

# Write a program which accept number from user and return number of digits in that number.
# Input => 145236           Output=> 6


def countDigit(n):
    count = 0
    if n < 0 :
        n = -1*n 

    if n == 0:
        count = 1

    while n != 0 :
        n= n//10
        count +=1
    
    print(count)

n = int(input("Enter the number : "))

countDigit(n)