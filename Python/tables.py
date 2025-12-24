
def generate_table(x: int, n: int) -> dict:
    dict = {}
    for i in range(1, n+1):
        dict[i] = x*i

    return dict

while True:
    num = int(input("Enter a number: "))
    if (num == -99):
        break


    else:
        ran = int(input("Enter length for multiplication: "))
        mult_dict = generate_table(num, ran)
        for key, value in mult_dict.items():
            print(f"{ran} X {key} = {value}")

