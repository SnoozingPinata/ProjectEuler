

def gen_triangular_number():
    counter = 0
    triangle_num = 0
    while True:
        counter += 1
        triangle_num += counter
        yield triangle_num


def get_factor_count(number):
    lower_bound = 2
    upper_bound = number
    count = 2
    while lower_bound < upper_bound:
        if number % lower_bound == 0:
            upper_bound = int(number / lower_bound)
            count +=2
        lower_bound += 1
    return count


if __name__ == "__main__":
    gen = gen_triangular_number()
    next(gen)
    highest_count = 0
    max_factor_count = 500

    while True:
        triangle_num = next(gen)
        count = get_factor_count(triangle_num)
        if count > max_factor_count:
            break

    print(f"Answer to Project Euler problem #12 is: {triangle_num}")