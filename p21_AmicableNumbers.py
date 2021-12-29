

def get_proper_divisors(number):
    proper_divisors = []
    for i in range(1, (round(number / 2) + 1)):
        if number % i == 0:
            proper_divisors.append(i)
    return proper_divisors

def add_number_list(number_list):
    running_total = 0
    for num in number_list:
        running_total += num
    return running_total

def get_sum_of_proper_divisors(number):
    return add_number_list(get_proper_divisors(number))

## problem is here. Can't think cause music is too loud. fix later
def parse_possible_pairs_map(possible_pairs_map):
    amicable_pairs_list = []
    for key in possible_pairs_map.keys():
        try:
            if key == possible_pairs_map[possible_pairs_map[key]]:
                amicable_pairs_list.append(key)
        except KeyError:
            pass
    return amicable_pairs_list

# could make this a lot smarter.
# could skip over odd numbers - I don't think it can have an amicable pair.
# could make a list of numbers that need to be tested, as each one is done, test its possible pair as well. 
#   add to list if they work and just remove from test wait list either way. -- probably smarter way to do it than fixing above function
def get_ans(upper_limit):
    possible_pairs_map = {}
    for num in range(2, upper_limit + 1, +2):
        potential_pair = get_sum_of_proper_divisors(num)
        possible_pairs_map.update({num: potential_pair})
    amicable_pair_numbers = parse_possible_pairs_map(possible_pairs_map)
    return add_number_list(amicable_pair_numbers)

if __name__ == "__main__":
    print(f"Answer to Project Euler problem #21 is: {get_ans(10000)}")