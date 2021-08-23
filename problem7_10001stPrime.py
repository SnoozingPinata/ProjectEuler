

def is_prime(number, preceding_prime_list):
    for prime in preceding_prime_list:
        if number % prime == 0:
            return False
    return True

prime_list = [2, 3]
current_num = prime_list[-1]
digit_to_find = 10001

while len(prime_list) < digit_to_find:
    if is_prime(current_num, prime_list):
        prime_list.append(current_num)
    current_num += 1

print(str(prime_list.pop()))