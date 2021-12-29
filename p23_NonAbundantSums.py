

def get_proper_divisors(number):
    proper_divisors = []
    for i in range(1, (round(number / 2) + 1)):
        if number % i == 0:
            proper_divisors.append(i)
    return proper_divisors

def is_abundant_number(number):
    return sum(get_proper_divisors(number)) > number

def get_abundant_number_list_below(upper_limit):
    abundant_numbers = []
    for num in range(12, upper_limit):
        if is_abundant_number(num):
            abundant_numbers.append(num)
    return abundant_numbers

def is_sum_of_abundant_numbers(number, abundant_number_list):
    for num in abundant_number_list:
        if num >= number:
            return False
        if number - num in abundant_number_list:
            return True

def get_ans(upper_limit):
    abundant_numbers = get_abundant_number_list_below(upper_limit)
    running_total = 0
    for num in range(1, upper_limit):
        if not is_sum_of_abundant_numbers(num, abundant_numbers):
            running_total += num
    return running_total


if __name__ == "__main__":
    print(f"Answer to Project Euler problem #23 is: {get_ans(28123 + 1)}")