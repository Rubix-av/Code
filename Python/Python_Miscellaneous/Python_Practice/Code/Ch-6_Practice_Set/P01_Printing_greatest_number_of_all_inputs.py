num1 = int(input("Enter the number-1: \n"))
num2 = int(input("Enter the number-2: \n"))
num3 = int(input("Enter the number-3: \n"))
num4 = int(input("Enter the number-4: \n"))

if(num4 > num1):
    f1 = num4
else:
    f1 = num1

if(num3 > num2):
    f2 = num3
else:
    f2 = num2

if(f1 > f2):
    print(num1, ",", num2, ",", num3, ",", num4, ":", str(
        f1) + " is greatest among these numbers")
else:
    print(num1, ",", num2, ",", num3, ",", num4, ":",
          str(f2) + " is greatest among these numbers")
