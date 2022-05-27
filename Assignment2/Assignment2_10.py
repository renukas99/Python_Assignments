

# Write a program which acceplt number from user and return addition of digits in that number.
# Input => 1452          Output => 12


def countDigit(n):
    sum = 0
    while (n>0):
        sum = sum + n%10
        n=n//10
    print("Sum of digits : ", sum)    

n = int(input("Enter the number : "))
countDigit(n)    