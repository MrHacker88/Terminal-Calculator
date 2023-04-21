Num1 = int(input("Enter Your First Number: "))
Num2 = int(input("Enter Your Second Number: "))

Add = Num1 + Num2 
Subtract = Num1 - Num2
Multiply = Num1 * Num2
Divide = Num1 / Num2
Remainder = Num1 % Num2
Exponent = Num1 ** Num2

print("Operation Availabe Are As Follows:-")

print("1.Addition")
print("2.Subtration")
print("3.Multiplication")
print("4.Division")
print("5.Find Remainder")
print("6.Exponentation")

print("Your Choice Is: ")
Opertion = int(input("1/2/3/4/5/6: "))

if Opertion == 1:
    print(f"The Answer is {Add}")
elif Opertion == 2:
    print(f"The Answer is {Subtract}")
elif Opertion == 3:
    print(f"The Answer is {Multiply}")
elif Opertion == 4:
    print(f"The Answer is {Divide}")
elif Opertion == 5:
    print(f"The Answer is {Remainder}")
elif Opertion == 6:
    print(f"The Answer is {Exponent}")
else:
    print("ERROR: INVALID OPERATOR SELECTED")
    print("KINDLY SELECT OPERTOR THAT ARE AVAILABLE")


