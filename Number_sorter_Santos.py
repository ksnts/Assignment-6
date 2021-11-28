num1=float(input("Input first number: "))
num2=float(input("Input second number: "))
num3=float(input("Input third number: "))
num4=float(input("Input fourth number: "))


if num1 >= num2 and num1 >=num3 and num1 >=num4:
    print(num1)
    if num2>=num3 and num2>=num4:
        print(num2)
    elif num3>=num2 and num3>=num4:
        print(num3)
    elif num4>=num2 and num4>=num3:
        print(num4)
 
