
# 1) Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for multiplication and Div() for division. 
#All functions accepts two parameters as number and perform the operation. Write on pytho program which call all the functions from Arithmetic module by accepting the 
#parameters from user.



num1 = int(input("Enter the First Number : "))
num2 = int(input("Enter the Second Number : "))

print("Enter which operation would you like to perform? : ")

char = input("Enter any of these char for specitic operation +, -,*,/ :")

result = 0

if char =='+':
    result = num1 + num2
    print("Addition is : ", result)

elif char == '-':
    result = num1 - num2
    print("Subtraction is : ", result)

elif char == '*':
    result = num1 * num2
    print("Multiplicatin is : ", result) 

elif char == '/':
    result = num1 / num2
    print("Division is : ", result)

else:
    print("Input character is not recognized : ")        


print(result)