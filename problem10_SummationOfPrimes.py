

# This is a complete mess and is nowhere near efficient as it can be.

def gen_primes():
    yield 2
    prime_list = [2]
    number = 1
    while True:
        is_prime = True
        number += 2
        for prime in prime_list:
            if number % prime == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(number)
            yield number


max_num = 2000000
prime_gen = gen_primes()
current_prime = next(prime_gen)
prime_list = [i for i in range(3, max_num, +2)]
prime_list.append(2)
not_prime_list = []

while current_prime < max_num:
    for x in range(current_prime + current_prime, max_num, +current_prime):
        not_prime_list.append(x)
    current_prime = next(prime_gen)

for non_prime in not_prime_list:
    if non_prime in prime_list:
        prime_list.remove(non_prime)

running_total = 0
for prime in prime_list:
    running_total += prime

print(running_total)