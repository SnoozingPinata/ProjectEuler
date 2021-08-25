

def gen_fibonacci_number(number_1, number_2):
    """
    Generate the next number in the fibonacci sequence given the last two terms of the sequence.

    number_1: Either 1 or the n-2th term of the sequence.

    number_2: Either 2 or the n-1th term of the sequence.
    """
    assert number_2 - number_1 == 1

    fib_1 = number_1
    fib_2 = number_2
    while True:
        fib_3 = fib_1 + fib_2
        yield fib_3
        fib_1, fib_2 = fib_2, fib_3

    
def sum_of_even_fibonnaci_numbers_below(upper_bound):
    """
    Find the sum of all even-valued fibonacci numbers below the given upper_bound.
    
    upper_bound: This is the limit for generated fibonnaci numbers. Only fibonacci numbers below this will be summed.
    """
    fib_gen = gen_fibonacci_number(0, 1)
    fib_num = next(fib_gen)
    running_total = 0
    while fib_num < upper_bound:
        if fib_num % 2 == 0:
            running_total += fib_num
        fib_num = next(fib_gen)
    return running_total


if __name__ == "__main__":
    print(f"Answer to Project Euler problem #4 is: {sum_of_even_fibonnaci_numbers_below(4000000)}")