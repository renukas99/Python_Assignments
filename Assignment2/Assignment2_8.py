
# Write a program which accept one number and display below pattern.
#Input => 5               # Below extra 6 program 
#1
#1 2 
#1 2 3
#1 2 3 4
#1 2 3 4 5
########################################################

def Number(x):
    for i in range(x):
        p = 1
        for j in range(i+1):
            print(p , end = " ")
            p+=1
        print("\n")    


x = int(input("Enter the number : "))      
Number(x)

##########################################################

# Dereasing Triangle

def Number(a):
    for i in range(a):
        p =1
        for i in range(i+1):
            print(" ", end = " ")
        for j in range(i,a):
            print(p, end = " ")
            p+=1
        print("\n")    

a = int(input("Enter the number : "))
Number(a)    

##############################################################

## Hill Pattern
def Number(b):
    for i in range(b):
        p=1
        for j in range(i,b):
            print(" ", end = " ")
        for j in range(i):
            print(p,end = " ")    
            p+=1

        for j in range(i+1):
            print(p , end = " ")    
            p+=1
        print("\n")    

b = int(input("Enter the number : "))        
Number(b)

################################################################

## 1 Decreasing Pattern

def Number(y):
    for i in range(y):
        p = y
        for j in range(i+1):
            print(p, end = " ")
            p-=1
        print(("\n"))    

y = int(input("Enter the number : "))    
Number(y)

################################################################

## 2

def Number(m):
    k = 5
    for i in range(m):
        p =k
        for j in range(i):
            print(" ", end = " ")

        for j in range(i,m):
            print(p, end = " ")    
            p-=1
        k-=1
        print("\n")   

m = int(input("Enter the number : "))        

Number(m)

###################################################################

##hil pattern like pyramide

def Number(r):
    for i in range(r):
        p =1
        for j in range(i,r):
            print(" ", end = " ")

        for j in range(i):
            print(p, end = " ")    
            p+=1

        for j in range(i+1):
            print(p, end = " ")
            p-=1

        print("\n")        
        

r = int(input("Enter the number : "))        
Number(r)

#################################################################

## Number pattern

def Number(d):
    p = 1
    for i in range(d):
        for j in range(i+1):
            print(p, end = " ")
            p+=1

        print("\n")    

d= int(input("Enter the number : "))
Number(d)