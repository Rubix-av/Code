# n = 5
# product = 1
# for i in range(n):
#     product = product * (i+1)

# print(product)

# def factorial_iter(n):
#     product = 1
#     for i in range(n):
#         product = product * (i+1)

#     return(product)

inp = int(input("Enter the number: "))

def factorial_recursive(n):
    if n == 1 or n == 0:    
        return 1

    return n * factorial_recursive(n-1)

# f = (factorial_iter(5))
r = factorial_recursive(inp)

# print(f)
print(r)
