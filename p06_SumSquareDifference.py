

def sum_of_squares(number_count):
    """Return the sum of the squares for the given amount of natural numbers."""
    result = 0
    for num in range(0, number_count+1, +1):
        result += num ** 2
    return result


def square_of_sum(number_count):
    """Return the square of the sum for the given amount of natural numbers."""
    sum = 0
    for num in range(0, number_count+1, +1):
        sum += num
    return sum ** 2


def difference_between(num1, num2):
    """Return the absolute difference between the given numbers."""
    return abs(num1 - num2)


def sum_square_difference(number_count):
    """Find the difference between the sum of the squares of the given amount of natural numbers and the square of the sum."""
    sum_of_squares_val = sum_of_squares(number_count)
    square_of_sum_val = square_of_sum(number_count)
    difference = difference_between(sum_of_squares_val, square_of_sum_val)
    return difference


if __name__ == "__main__":
    print(f"Answer to Project Euler problem #6 is: {sum_square_difference(100)}")