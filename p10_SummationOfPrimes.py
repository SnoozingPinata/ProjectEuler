

def sum_of_primes(max_number):
    """Return the sum of the given list of primes."""
    return sum(create_prime_list_below(max_number))


def create_prime_list_below(max_number):
    """Return a list of primes below the given number."""
    # Create a boolean array representing a number line.
    number_line = [True for i in range(0, max_number + 1)]

    # Set the values representing 0 and 1 to False.
    number_line[0], number_line[1] = False, False
    prime_list = []

    # Iterate through the number_line and test if each value is True(representing prime).
    # If it's prime, iterate through the rest of the number_line and set each multiple to False.
    for i in range(0, max_number):
        if number_line[i] == True:
            prime_list.append(i)
            for index in range(i + i, max_number + 1, +i):
                number_line[index] = False
    return prime_list
    

if __name__ == "__main__":
    print(f"Answer to Project Euler problem #10 is: {sum_of_primes(2000000)}")