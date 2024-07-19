def odd_even(l: list[int]) -> list[bool]:
    result_list: list[bool] = []

    for num in l:
        if num%2 == 0:
            result_list.append(True)
        else:
            result_list.append(False)

    return result_list

num_list = [2,5,4,7,3,8,1,36,23]
print(odd_even(num_list))
