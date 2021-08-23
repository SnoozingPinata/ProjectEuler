

def gen_triangular_number():
    counter = 0
    triangle_num = 0
    while True:
        counter += 1
        triangle_num += counter
        yield triangle_num

def gen_primes():
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

gen = gen_triangular_number()
next(gen)

prime_gen = gen_primes()


divisors_over = 5
num_dict = {1: [1]}
while True:
    triangle_num = next(gen)
    factors_list = []
    prime_list = [2]
    factors_list.append(triangle_num)
    while triangle_num > prime_list[-1]:
        prime_list.append(next(prime_gen))
    for key in num_dict.keys():
        if triangle_num % key == 0:
            for factor in num_dict[key]:
                if not factor in factors_list:
                    factors_list.append(factor)
    for prime in prime_list:
        if triangle_num % prime == 0:
            if not prime in factors_list:
                factors_list.append(prime)
    if len(factors_list) > divisors_over:
        print("Num: " + str(triangle_num))
        print("factors: ")
        print(factors_list)
        print("Answer is: " + str(triangle_num))
        break
    print("Num: " + str(triangle_num))
    print("factors: ")
    print(factors_list)
    num_dict.update({triangle_num: factors_list})