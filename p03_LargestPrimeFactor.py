

def gen_factors(number):
    if number == 1:
        yield 1
    yield number
    factors = [1, number]
    lower_bound = 2
    upper_bound = number
    count = 2
    while lower_bound < upper_bound:
        if number % lower_bound == 0:
            factors.append(lower_bound)
            upper_bound = int(number / lower_bound)
            factors.append(upper_bound)
            count +=2
        lower_bound += 1
    return factors