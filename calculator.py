
print("Enter numbers:")
num1, num2 = map(int, input().split())

print("Enter operation to perform:")
print("+  -  *  /  %  //  **")

o = input()

if o == '+':
    print(f'{num1} + {num2}:', num1 + num2)

elif o == '-':
    print(f'{num1} - {num2}:', num1 - num2)

elif o == '*':
    print(f'{num1} * {num2}:', num1 * num2)

elif o == '/':
    if num2 != 0:
        print(f'{num1} / {num2}:', num1 / num2)
    else:
        print("Division by zero is not allowed")

elif o == '%':
    if num2 != 0:
        print(f'{num1} % {num2}:', num1 % num2)
    else:
        print("Modulus by zero is not allowed")

elif o == '//':
    if num2 != 0:
        print(f'{num1} // {num2}:', num1 // num2)
    else:
        print("Floor division by zero is not allowed")

elif o == '**':
    print(f'{num1} ** {num2}:', num1 ** num2)

else:
    print("Invalid operator")
