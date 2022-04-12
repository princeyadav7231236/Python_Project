print("Calculator")
num1 = int(input("Enter First number : "))
sign = input("Enter the operator")
num2 = int(input("Enter Second number : "))

if sign == "+" and num1 == 56 and num2 == 9:
    print("The SUM is : ", "77")
elif sign == "+":
    print("The SUM is : ", num1 + num2)
elif sign == "*" and num1 == 45 and num2 == 3:
    print("The PRODUCT is : ", "555")
elif sign == "*":
    print("The PRODUCT is : ", num1 * num2)
elif sign == "/" and num1 == 56 and num2 == 6:
    print("The DIVISION is : ", "4")
elif sign == "/":
    print("The DIVISION is : ", num1 / num2)
elif sign == "-":
    print("The DIFFERENCE is : ", num1 - num2)
else:
    print("You entered a wrong input ")
