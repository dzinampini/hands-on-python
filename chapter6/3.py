number = int(input("Enter the number to find its factorial:"))
i = 1
factorial = 1
while i <= number:
    factorial = factorial * i
    print("Product at the end of iteration", i, "is", factorial)
    i = i + 1
print("The factorial of the number", number, "is", factorial)
