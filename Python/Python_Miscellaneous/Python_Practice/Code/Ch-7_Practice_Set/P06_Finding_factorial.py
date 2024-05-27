num = int(input("Enter the number here: "))

factorial = 1

for i in range(1, num+1):
    factorial = factorial * i

print(f"The factorial of {num} is {factorial}")