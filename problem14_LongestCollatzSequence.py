

def is_even(number):
    """Return true if the number given is even. Return False if it is odd."""
    if number % 2 == 0:
        return True
    else:
        return False

def get_next_collatz(number):
    """Return the next number in the Collatz Sequence given a starting number."""
    if is_even(number):
        return number // 2
    else:
        return 3 * number + 1

def gen_collatz_number(starting_number):
    next_num = get_next_collatz(starting_number)
    yield next_num
    while True:
        next_num = get_next_collatz(next_num)
        yield next_num

def update_collatz_dict(collatz_dict, collatz_sequence):
    if collatz_sequence[0] not in collatz_dict.keys():
        collatz_dict.update({collatz_sequence[0]: len(collatz_sequence)})
    return collatz_dict

def get_collatz_sequence(starting_num, collatz_dict):
    collatz_sequence = [starting_num]
    gen = gen_collatz_number(starting_num)
    current_num = starting_num
    while current_num != 1 and current_num not in collatz_dict.keys():
        current_num = next(gen)
        collatz_sequence.append(current_num)
    updated_dict = update_collatz_dict(collatz_dict, collatz_sequence)
    return updated_dict

def get_ans(collatz_dict):
    key_list = list(collatz_dict.keys())
    value_list = list(collatz_dict.values())
    max_value = max(value_list)
    max_value_index = value_list.index(max_value)
    val = key_list[max_value_index]
    return val

def find_longest_collatz_sequence_under(max_number):
    # starting num, sequence count
    collatz_dict = {1: 1}
    index = 1
    while index < max_number:
        collatz_dict = get_collatz_sequence(index, collatz_dict)
        index += 1
        print(index)
    return get_ans(collatz_dict)


if __name__ == "__main__":
    print(f"Answer to Project Euler problem #14 is: {find_longest_collatz_sequence_under(1000000)}")

# getting 626331 but it's not right.