

def get_proper_divisors(number):
    proper_divisors = []
    for i in range(1, (round(number / 2) + 1)):
        if number % i == 0:
            proper_divisors.append(i)
    return proper_divisors

def get_sum_of_proper_divisors(number):
    return sum(get_proper_divisors(number))

def get_ans(upper_limit):
    # this basically does all the work twice
    # could make a number list and cross of numbers when they are evaluated early
    #   (this happens when a number is a pair)
    running_total = 0
    for num in range(2, upper_limit, +2):
        possible_pair = get_sum_of_proper_divisors(num)
        if num == get_sum_of_proper_divisors(possible_pair) and num != possible_pair:
            running_total += num
            running_total += possible_pair
    return int(running_total / 2)
    

if __name__ == "__main__":
    print(f"Answer to Project Euler problem #21 is: {get_ans(10000)}")