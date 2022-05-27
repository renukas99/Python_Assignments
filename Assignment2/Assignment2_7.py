

# Write a below program which accept one number and display below pattern.

# Input => 5
#  1 2 3 4 5
#  1 2 3 4 5
#  1 2 3 4 5
#  1 2 3 4 5
#  1 2 3 4 5

def Number(n):
    
    for i in range(1, n+1, 1):
        for j in range(1, n+1, 1):
            print(j, end = " ")

        print("\n")

n = int(input("Enter the number : "))        

Number(n)

############################################################################

def Number(x):
    for i in range(1,x+1,1):
        for j in range(1,x+1,1):
            print(i, end = " ")
        print("\n")    

x = int(input("Enter the number : "))        

Number(x)