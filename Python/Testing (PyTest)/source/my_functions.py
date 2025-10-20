def add(number_one: int, number_two: int):
    return number_one + number_two


def divide(number_one: int, number_two: int):
    if number_two == 0:
        raise ValueError
    return number_one / number_two