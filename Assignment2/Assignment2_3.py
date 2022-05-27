

# Write a program which accpet one number from user and retrun its factorial.

def Factorial(x):
    if x == 0 :
        return 1

    else:
        return x * Factorial(x-1)    

x = int(input("Enter the number : "))        
print(Factorial(x))

Factorial(x)


# 5=> 5*4*3*2*1 = 120
# 10=> 10*9*8*7*6*5*4*3*2*1 = 3628800