#user inputs the 4 numbers
num1=float(input("Input first number: "))
num2=float(input("Input second number: "))
num3=float(input("Input third number: "))
num4=float(input("Input fourth number: "))

#multiple nested if else conditions to determine order
if num1 >= num2 and num1 >=num3 and num1 >=num4:
    print(num1)
    if num2>=num3 and num2>=num4:
        print(num2)
        if num3>=num4:
            print(num3)
            print(num4)
        else:
            print(num4)
            print(num3)
            
    elif num3>=num2 and num3>=num4:
        print(num3)
        if num2>=num4:
            print(num2)
            print(num4)
        else:
            print(num4)
            print(num2)
           
    elif num4>=num3 and num4>=num2:
        print(num4)
        if num3>=num2:
            print(num3)
            print(num2)
        else:
            print(num2)
            print(num3)
            

elif num2 >= num1 and num2 >=num3 and num2 >=num4:
    print(num2)
    if num1>=num3 and num1>=num4:
        print(num1)
        if num3>=num4:
            print(num3)
            print(num4)
        else:
            print(num4)
            print(num3)
            
    elif num3>=num1 and num3>=num4:
        print(num3)
        if num1>=num4:
            print(num1)
            print(num4)
        else:
            print(num4)
            print(num1)
            
    elif num4>=num1 and num4>=num3:
        print(num4)
        if num1>=num3:
            print(num1)
            print(num3)
        else:
            print(num3)
            print(num1)
            

elif num3 >= num1 and num3 >=num2 and num3 >=num4:
    print(num3)
    if num1>=num2 and num1>num4:
        print(num1)
        if num2>=num4:
            print(num2)
            print(num4)
        else:
            print(num4)
            print(num2)
    elif num2>=num1 and num2>=num4:
        print(num2)
        if num1>=num4:
            print(num1)
            print(num4)
        else:
            print(num4)
            print(num1)
    elif num4>=num1 and num4>=num2:
        print(num4)
        if num1>=num2:
            print(num1)
            print(num2)
        else:
            print(num2)
            print(num1)

elif num4 >= num1 and num4 >=num2 and num4 >=num3:    
    print(num4)
    if num1>=num2 and num1>=num3:
        print(num1)
        if num2>=num3:
            print(num2)
            print(num3) 
        else:
            print(num3)
            print(num2)
    elif num2>=num1 and num2>=num3:
        print(num2)
        if num1>=num3:
            print(num1)
            print(num3)
        else:
            print(num3)
            print(num1)
    elif num3>=num1 and num3>=num2:
        print(num3)
        if num1 >=num2:
            print(num1)
            print(num2)
        else:
            print(num2)
            print(num1)




    
 
