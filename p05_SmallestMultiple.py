

# This function tries to disqualify the given number as quickly as possible by working backwards down the divisor_list.
def is_multiple_of_all_list_members(number, divisor_list):
    """Test if the given number is evenly divisible by the given divisor_list."""
    for index in range(len(divisor_list) - 1, 0, -1):
        if number % divisor_list[index] != 0:
            return False
    return True


# This is a strong optimization. Using divisibility rules, the optimal increment value can be determined.
# The given problem and the test case both must be divisible by 10 so only checking values that can be divisible by 10 is much faster.
# Could remove values from the divisor_list based on what number is being incremented. For example, when incrementing by 10,
# every number is going to be divisible by 10, so there's no reason to check for it. 
# This could be greatly expanded upon by checking the divisibility of each value in the list before returning a value.
def find_increment_value(divisor_list):
    """Find the optimal increment value based on divisibility rules and the given divisor_list."""
    if 10 in divisor_list:
        return 10 
    elif 5 in divisor_list:
        return 5
    elif 6 in divisor_list:
        return 2
    elif 2 in divisor_list:
        return 2
    else:
        return 1


def find_smallest_multiple(divisor_list):
    """
    Find the smallest number that is evenly divisible by all of the numbers in the given divisor_list.
    
    divisor_list: A list of divisors sorted from lowest to highest.
    """
    increment_value = find_increment_value(divisor_list)
    number = increment_value
    while True:
        if is_multiple_of_all_list_members(number, divisor_list):
            return number
        number += increment_value


if __name__ == "__main__":
    print(f"Answer to Project Euler problem #5 is: {find_smallest_multiple(range(1,20))}")