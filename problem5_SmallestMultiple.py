
number_found = False

divisor_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
number = divisor_list[-1]

def is_multiple(number, divisor):
    return number % divisor == 0

def is_multiple_of_list(number, divisor_list):
    for divisor in divisor_list:
        if is_multiple(number, divisor):
            pass
        else:
            return False
    return True

while not number_found:
    if is_multiple_of_list(number, divisor_list):
        smallest_multiple = number
        number_found = True
        continue
    else:
        number += 1

print(smallest_multiple)

# Could probably make this a lot more efficient just by cutting the divisor list down (if divisible by 15, it's divisible by 3 and 5)
# and by sorting the divisor list by likelihood of success (19 first number in list) 