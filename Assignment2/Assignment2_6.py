

# Write a program which accept one number and display below pattern.
#input = 5
# * * * * *
# * * * *
# * * *
# * *
# *
##########################################################################

def printPattern(x):
    for i in range(x):
        for j in range(i,x):
            print("*", end = " ")
        print("\n")    
    
x = int(input("Enter the number  : "))    

printPattern(x)

#########################################################

def printPattern(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end = " ")
        print("\n")    
    
n = int(input("Enter the number  : "))    

printPattern(n)

###########################################################

def printPattern(a):
    for i in range(a):
        for s in range(-a,-i):
            print(" ", end = " ")

        for j in range(i+1):
            print("*", end = " ")
        print("\n")    
    
a = int(input("Enter the number  : "))    

printPattern(a)

#############################################################

def printPattern(b):
    for i in range(b):
        for s in range(i):
            print(" ", end = " ")

        for j in range(i, b):
            print("*", end = " ")
        print("\n")    
    
b = int(input("Enter the number  : "))    

printPattern(b)

###############################################################

def printPattern(c):
    k = c -1

    for i in range (0,c):
        for j in range(0,k):
            print(end = " ")

        k = k-1

        for j in range(0, i+1):
            print("*", end = " ")

        print("\n")       
c = int(input("Enter the number : "))             

printPattern(c)





