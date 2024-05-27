inp = int(input("Enter a number: "))

def sumN(n):
    if n == 1:
        return 1
    return sumN(n-1) + n

x = sumN(inp)
print(x)
