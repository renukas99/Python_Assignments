

#  Write a program which accept one number form user and return addition of its factors.

def Factors(x):
    for i in range(1, x+1):
        if x % i == 0:
            print(i)

x = int(input("Enter the number : "))            
#print(Factors(x))

Factors(x)