

def is_prime(number, preceding_prime_list):
    """Test if the given number is prime given a list of all primes before the given number."""
    for prime in preceding_prime_list:
        if number % prime == 0:
            return False
    return True


def find_nth_prime(position):
    """Find the nth prime."""
    prime_list = [2, 3]
    current_num = prime_list[-1]
    counter = 2
    while counter < position:
        if is_prime(current_num, prime_list):
            prime_list.append(current_num)
            counter += 1
        current_num += 1
    return prime_list.pop()


if __name__ == "__main__":
    print(f"Answer to Project Euler problem #7 is: {find_nth_prime(10001)}")