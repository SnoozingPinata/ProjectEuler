

def is_palindrome(test_string):
    """
    Test Input to determine if it is a palindrome. Return a boolean value.

    test_string: A string or a value that can be converted to a string.
    """
    if not isinstance(test_string, str):
        test_string = str(test_string)

    if len(test_string) <= 1:
        return True
    elif test_string[0] != test_string[-1]:
        return False
    else:
        return is_palindrome(test_string[1:-1])


def gen_palindrome_number_lower_than(upper_bound):
    """
    Find the next number that is a palindrome that is less than or equal to upper_bound.

    upper_bound: An int.
    """
    assert isinstance(upper_bound, int)
    while True:
        if is_palindrome(upper_bound):
            yield upper_bound
        upper_bound -= 1


def find_largest_palindrome_product(digit_count):
    """
    Find the largest palindrome made from the product of two <digit_count> numbers.

    digit_count: An int that specifies the maximum amount of digits each factors can have.
    """
    largest_number_in_digit_count_limit = int('9' * digit_count)
    iterator = largest_number_in_digit_count_limit
    upper_bound = largest_number_in_digit_count_limit * largest_number_in_digit_count_limit
    palindrome_generator = gen_palindrome_number_lower_than(upper_bound)
    while True:
        palindrome_number = next(palindrome_generator)
        for num in range(iterator, 0, -1):
            palindrome_is_product_of_iterator = palindrome_number % num == 0
            factors_in_range = palindrome_number / num < largest_number_in_digit_count_limit
            if palindrome_is_product_of_iterator and factors_in_range:
                return palindrome_number


if __name__ == "__main__":
    print(f"Answer to Project Euler problem #4 is: {find_largest_palindrome_product(3)}")