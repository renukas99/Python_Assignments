

# Write a programm which accept one number for user and check whether number is prime or not.

def Prime(x):
    if x > 1 :
        for i in range(2,x):
            if (x%i) == 0:
                print("Number is not prime : ", x)
                break
        else : 
            print("Number is prime : ",x)
    else :
        print("Number is not prime : ")

x = int(input("Enter the number : "))                    

Prime(x)