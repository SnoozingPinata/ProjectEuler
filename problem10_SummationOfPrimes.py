

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

gen = gen_primes()
max_value = 2000000
running_total = 0

while True:
    num = next(gen)
    print(num)
    if num >= max_value:
        break
    running_total += num

print(running_total)