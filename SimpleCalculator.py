Fnumber = int(input("Enter your first number; "))
Snumber = int(input("Enter your second number; "))
Operator = input("Enter an operator(+,-,*,/); ")
if Operator == '+':
    print(Fnumber + Snumber)
elif Operator == '-':
    print(Fnumber - Snumber) 
elif  Operator == '*':
    print(Fnumber * Snumber)
elif Operator == '/':
    print(Fnumber / Snumber)
else:
    print(Error)
