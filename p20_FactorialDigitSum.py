

def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)

def add_numbers_digits(number):
    string_num = str(number)
    running_total = 0
    for char in string_num:
        running_total += int(char)
    return running_total

def get_ans(number):

    factorial_value = factorial(number)
    ans = add_numbers_digits(factorial_value)
    return ans


if __name__ == "__main__":
    print(f"Answer to Project Euler problem #20 is: {get_ans(100)}")