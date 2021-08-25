

def is_prime(number):
    """Test if the given number is prime."""
    lower_bound = 2
    upper_bound = number
    count = 2
    while lower_bound < upper_bound:
        if number % lower_bound == 0:
            upper_bound = int(number / lower_bound)
            count +=2
        lower_bound += 1
    return count == 2


def get_factors(number):
    """Return a list of factors for the given number."""
    if number == 1:
        return [1]
    factors = [1, number]
    lower_bound = 2
    upper_bound = number
    while lower_bound < upper_bound:
        if number % lower_bound == 0:
            factors.append(lower_bound)
            upper_bound = int(number / lower_bound)
            factors.append(upper_bound)
        lower_bound += 1
    return factors


def largest_prime_factor(number):
    """Find the largest prime factor for the given number."""
    factor_list = get_factors(number)
    highest_factor = 1
    for factor in factor_list:
        if is_prime(factor) and factor > highest_factor:
            highest_factor = factor
    return highest_factor


if __name__ == "__main__":
    print(f"Answer to Project Euler problem #3 is: {largest_prime_factor(600851475143)}")